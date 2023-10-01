import tkinter as tk

import ttkbootstrap as ttk
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QTableWidgetItem


class Task:
    def __init__(self, target, money, date_in, date_out, type, remark=None):
        self.target = target
        self.money = money
        self.date_in = date_in
        self.date_out = date_out
        self.type = type
        self.remark = remark

    def __repr__(self):
        return f"target={self.target},\nmoney={self.money}, \
            \ndate_in={self.date_in}, \ndate_out={self.date_out}, \
            \ntype={self.type}, \nremark={self.remark}"


    def tableAdd(self, table):
        table.insertRow(0)

        table.setItem(0, 0, QTableWidgetItem(self.target))
        table.setItem(0, 1, QTableWidgetItem(self.money))
        table.setItem(0, 2, QTableWidgetItem(self.date_in))
        table.setItem(0, 3, QTableWidgetItem(self.date_out))
        table.setItem(0, 4, QTableWidgetItem(self.type))
        table.setItem(0, 5, QTableWidgetItem(self.remark))

        # 设置文本居中
        for row in range(table.rowCount()):
            for column in range(table.columnCount()):
                item = table.item(row, column)
                if item is not None:
                    item.setTextAlignment(Qt.AlignCenter)
