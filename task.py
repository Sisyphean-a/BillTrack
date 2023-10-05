import datetime
import time

from PySide6 import QtGui
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QTableWidgetItem


class Task:
    def __init__(self, target, money, date_in, date_out, type, remark=None):
        time.sleep(0.0001)
        current_milli_time = lambda: int(round(time.time() * 1000))
        self.id = str(current_milli_time())
        self.target = target
        self.money = money
        self.date_in = date_in
        self.date_out = date_out
        self.type = type
        self.remark = remark
        self.status = "new"

    def __repr__(self):
        return f"target={self.target},\nmoney={self.money}, \
            \ndate_in={self.date_in}, \ndate_out={self.date_out}, \
            \ntype={self.type}, \nremark={self.remark},\nstatus={self.status}"

    def set_status(self, status):
        self.status = status

    def set_id(self, id):
        self.id = id

    def tableAdd(self, table):
        table.insertRow(0)

        table.setItem(0, 0, QTableWidgetItem(self.target))
        table.setItem(0, 1, QTableWidgetItem(self.money))
        table.setItem(0, 2, QTableWidgetItem(self.date_in))
        table.setItem(0, 3, QTableWidgetItem(self.date_out))
        table.setItem(0, 4, QTableWidgetItem(self.type))
        table.setItem(0, 5, QTableWidgetItem(self.remark))
        table.setItem(0, 6, QTableWidgetItem(self.id))

        # 设置文本居中
        for row in range(table.rowCount()):
            for column in range(table.columnCount()):
                item = table.item(row, column)
                if item is not None:
                    item.setTextAlignment(Qt.AlignCenter)

        # 获取money值和date值以及今天的时间以及时间差
        money = int(table.item(0, 1).text())
        date = table.item(0, 3).text()
        date = datetime.datetime.strptime(date, "%Y/%m/%d")
        today = datetime.datetime.today()
        diff = (today - date).days
        print(diff)

        if diff <= 3:
            for colume in range(table.columnCount()):
                # 设置当前行的背景颜色
                table.item(0, colume).setBackground(QtGui.QColor(255, 100, 97))
                # 设置当前行的字体颜色
                table.item(0, colume).setForeground(QtGui.QColor(255, 255, 255))
                # 设置当前行的字体加粗
                # table.item(0, 1).setFontWeight(QtGui.QFont.Bold)

        # 判断money是否大于100000
        if money >= 100000 and diff <= 30:
            for colume in range(table.columnCount()):
                # 设置当前行的背景颜色
                table.item(0, colume).setBackground(QtGui.QColor(255, 0, 0))
                # 设置当前行的字体颜色
                table.item(0, colume).setForeground(QtGui.QColor(255, 255, 255))
                # 设置当前行的字体加粗
                # table.item(0, 1).setFontWeight(QtGui.QFont.Bold)
