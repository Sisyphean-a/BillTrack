import time
from datetime import datetime, timedelta

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

    def new_time(self):
        # 获取当前日期
        current_date = datetime.now()
        # 将日期对象格式化为字符串并返回
        self.date_in = current_date.strftime("%Y/%m/%d")

        # 将日期字符串转换为datetime对象
        date = datetime.strptime(self.date_out, "%Y/%m/%d")
        # 计算下个月的日期
        next_month = date.replace(month=date.month + 1)
        # 处理年份和月份的进位
        if next_month.month == 1:
            next_month = next_month.replace(year=next_month.year + 1)
        # 将日期对象转换为字符串并返回
        self.date_out = next_month.strftime("%Y/%m/%d")

    def tableAdd(self, table):
        table.insertRow(0)

        # 创建一个列表，按顺序存储表格的列信息，一个元素对应一列
        items = [
            self.target,
            self.money,
            self.date_in,
            self.date_out,
            self.type,
            self.remark,
            self.id,
        ]

        for i in range(len(items)):
            table.setItem(0, i, QTableWidgetItem(items[i]))

        # 设置文本居中
        for row in range(table.rowCount()):
            for column in range(table.columnCount()):
                item = table.item(row, column)
                if item is not None:
                    item.setTextAlignment(Qt.AlignCenter)

        # 获取money值和date值以及今天的时间以及时间差
        money = int(table.item(0, 1).text())
        date = table.item(0, 3).text()
        date = datetime.strptime(date, "%Y/%m/%d")
        today = datetime.today()
        diff = (date - today).days

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

        if table.objectName() == "Table_old":
            for colume in range(table.columnCount()):
                # 设置当前行的字体颜色
                table.item(0, colume).setForeground(QtGui.QColor(0, 0, 0))
