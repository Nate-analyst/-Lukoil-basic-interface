import sys
import os
import PySide6
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QListWidgetItem, QMessageBox
from PySide6 import QtCore
from PySide6 import QtCharts
from mainwindow import Ui_MainWindow
from edit_dialog import Ui_Dialog
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session
from statistics import *

dirname = os.path.dirname(PySide6.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path


class EditDialog(QDialog):
    def __init__(self, indicators, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.btnAdd.clicked.connect(self.accept)
        self.ui.btnCancel.clicked.connect(self.reject)
        
        for i in indicators.values():
            self.ui.cmbIndicator.addItem(i.title, i)
    
    def get_data(self):
        return {
            'indicator_id': self.ui.cmbIndicator.currentData().indicators_id,
            'year': self.ui.txtYear.text(),
            'value': self.ui.txtValue.text()
        }
    

class UpdateDialog(EditDialog):
    def __init__(self, indicators, init_data, *args, **kwargs) -> None:
        super().__init__(indicators, *args, **kwargs)

        self.ui.btnAdd.setText('Edit')
        self.ui.cmbIndicator.setEnabled(False)

        indicator_name = indicators[init_data.indicators_id].title
        self.ui.cmbIndicator.setCurrentText(indicator_name)
        self.ui.txtValue.setText(str(init_data.value))
        self.ui.txtYear.setText(str(init_data.year))



class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.engine = create_engine("sqlite+pysqlite:///Database.db", echo=True)

        self.load_indicators()
        self.load_years()
        self.load_values()

        self.ui.cmbIndicator.currentIndexChanged.connect(self.load_values)
        self.ui.cmbYear.currentIndexChanged.connect(self.load_values)
        self.ui.btnAdd.clicked.connect(self.on_btnAdd_click)
        self.ui.btnRemove.clicked.connect(self.on_btn_Remove_click)
        self.ui.btnEdit.clicked.connect(self.on_btn_Edit_click)


    def on_btn_Edit_click(self):
        item = self.ui.lstitems.currentItem()
        init_data = item.data(QtCore.Qt.ItemDataRole.UserRole)

        dialog = UpdateDialog(self.indicators, init_data)
        r = dialog.exec()
        if r == 0:
            return
        
        data = dialog.get_data()
        with Session(self.engine) as s:
            query = '''
            UPDATE indic_values
            SET year = :y, value = :v
            WHERE values_id = :id
            '''
            s.execute(text(query), {
                'y': data['year'],
                'v': data['value'],
                'id': init_data.values_id
            })
            s.commit()

        self.load_indicators()
        self.load_years()



    def on_btn_Remove_click(self):
        item = self.ui.lstitems.currentItem()
        data = item.data(QtCore.Qt.ItemDataRole.UserRole)

        confirm = QMessageBox.question(self, 'Delete', 'Are you sure?')
        if confirm == QMessageBox.StandardButton.No:
            return
        
        with Session(self.engine) as s:
            query = """
            DELETE 
            FROM indic_values 
            WHERE values_id = :id
            """
            
            s.execute(text(query), {"id": data.values_id})
            s.commit()

        self.load_indicators()
        self.load_years()


    def on_btnAdd_click(self):
        dialog = EditDialog(self.indicators)
        i = dialog.exec()
        if i == 0:
            return
        data = dialog.get_data()
        with Session(self.engine) as s:
            query = '''
            INSERT INTO indic_values(indicators_id, year, value)
            VALUES (:ind, :y, :v)
            '''

            s.execute(text(query), {
                'ind': data['indicator_id'],
                'y': data['year'],
                'v': data['value'],
            })
            s.commit()
        
        self.load_values()
        self.load_years()



    def load_values(self):
        indicators_data = self.ui.cmbIndicator.currentData()
        if indicators_data:
            indicators_id = self.ui.cmbIndicator.currentData().indicators_id
        else:
            indicators_id = 0
        
        year = self.ui.cmbYear.currentText()

        self.ui.lstitems.clear()
        self.rows = []

        with Session(self.engine) as s:
            query = """
            SELECT *
            FROM indic_values 
            WHERE (:ind = 0 OR indicators_id = :ind)
                    AND (:y = 'All years' OR year = :y)
            """
            rows = s.execute(text(query), {"ind": indicators_id, "y": year})
            for r in rows:
                indicator_name = self.indicators[r.indicators_id].title 
                item = QListWidgetItem(f"{indicator_name}, {r.year}, {r.value}")
                item.setData(QtCore.Qt.ItemDataRole.UserRole, r)
                self.ui.lstitems.addItem(item)
                self.rows.append(r)
                
        self.show_statistics()
        self.draw_bar_chart()    

    def draw_bar_chart(self):
        self.data_by_indicators = {}

        years = set()
        for row in self.rows:
            items = self.data_by_indicators.setdefault(row.indicators_id, {})
            items[row.year] = row.value
            years.add(row.year)
        
        years = sorted(years)

        series = QtCharts.QBarSeries()
        for indicators_id, indicator_data in self.data_by_indicators.items():
            indicator_title = self.indicators[indicators_id].title
            bar_set = QtCharts.QBarSet(indicator_title)
            for year in years:
                value = indicator_data.get(year, 0)
                bar_set.append(value)

            series.append(bar_set)

        chart = QtCharts.QChart()
        chart.addSeries(series)
        chart.createDefaultAxes()

        axis = QtCharts.QBarCategoryAxis()
        axis.append([str(i) for i in years])
        chart.setAxisX(axis)
        series.attachAxis(axis)

        self.ui.chartView.setChart(chart)
            


    def show_statistics(self):
        query = """
        SELECT *
        FROM indic_values
        WHERE (year = :y)
        ORDER BY year DESC
        """

        year = self.ui.cmbYear.currentText()
        if year == 'All years':
            year = '2021'
        with Session(self.engine) as s:
            rows = s.execute(text(query), {"y": year})

            indicator_values = {}
            for r in self.rows:
                indicator_values[r.indicators_id] = r.value
            value1 = round(indicator_values[1] / indicator_values[2] * 100, 2)
            value2 = round(indicator_values[1] / indicator_values[3] * 100, 2)
            value3 = round(indicator_values[1] / indicator_values[4] * 100, 2)
            value4 = round(indicator_values[1] / indicator_values[5] * 100, 2)
            value5 = round(indicator_values[1] / indicator_values[6] * 100, 2)
            value6 = round(indicator_values[1] / indicator_values[7] * 100, 2)

        self.ui.lblStatistics.setText(f"""
        Profitability indicators PJSC "Lukoil" for <b style="color: red; font-size: 14px">{year}</b> is: 
        <hr>
        Profitability of assets: <b style="color: blue; font-size: 14px">{value1}%</b>
        <hr>
        Profitability of sales: <b style="color: blue; font-size: 14px">{value2}%</b>
        <hr>
        Profitability of basic production assets: <b style="color: blue; font-size: 14px">{value3}%</b>
        <hr>
        Profitability of сurrent assets: <b style="color: blue; font-size: 14px">{value4}%</b>
        <hr>
        Profitability of capital: <b style="color: blue; font-size: 14px">{value5}%</b>
        <hr>
        Profitability of investments: <b style="color: blue; font-size: 14px">{value6}%</b>
        """)           


    def load_indicators(self):
        self.indicators = {}
        with Session(self.engine) as s:
            query = """
            SELECT *
            FROM indicators
            """

            rows = s.execute(text(query))
            for r in rows:
                self.indicators[r.indicators_id] = r

        self.ui.cmbIndicator.addItem('All indicators')
        for r in self.indicators.values():
            self.ui.cmbIndicator.addItem(r.title, r)

    def load_years(self):
        self.ui.cmbYear.clear()
        self.ui.cmbYear.addItem('All years')

        with Session(self.engine) as s:
            query = '''
            SELECT DISTINCT year
            FROM indic_values
            '''

            rows = s.execute(text(query))
            for r in rows:
                self.ui.cmbYear.addItem(str(r.year))  


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())