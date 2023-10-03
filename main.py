from PySide6.QtCore import QDate, Qt
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QAbstractItemView, QApplication

from task import Task
from task_list import TaskList


class Main:
    def __init__(self):
        # 从文件中加载UI定义
        self.ui = QUiLoader().load("bill.ui")
        self.ui.AddTodoButton.clicked.connect(self.addTodo)
        self.ui.FinishTodoButton.clicked.connect(self.finishTodo)

        # 设置表格相关属性，不可编辑、整行选中、排序功能、隐藏id列
        self.ui.Table.horizontalHeader().setStretchLastSection(True)
        self.ui.Table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.Table.setSortingEnabled(True)
        self.ui.Table.setColumnHidden(6, True)
        self.ui.Table_old.horizontalHeader().setStretchLastSection(True)
        self.ui.Table_old.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.Table_old.setSortingEnabled(True)
        self.ui.Table_old.setColumnHidden(6, True)

        # 设置初始化时间为当前时间
        currentDate = QDate.currentDate()
        self.ui.InDateEdit.setDate(currentDate)
        self.ui.InDateEdit.setCalendarPopup(True)
        self.ui.OutDateEdit.setDate(currentDate)
        self.ui.OutDateEdit.setCalendarPopup(True)

        # 初始化表格
        self.taskList = TaskList()
        self.update_table_ui()

    def addTodo(self):
        # 从信息栏中获取信息
        Target = self.ui.ObjectEdit.text()
        Money = self.ui.MoneyEdit.text()
        DateIn = self.ui.InDateEdit.text()
        DateOut = self.ui.OutDateEdit.text()
        Type = self.ui.TypeEdit.currentText()
        Remark = self.ui.RemarkEdit.text()

        # 对信息栏进行判断
        if Target == "" or Money == "" or DateIn == "" or DateOut == "" or Type == "":
            self.update_text(self.ui.MessageLabel, "账单消息不完整\n添加失败")
            return

        # 创建task对象
        task = Task(
            target=Target,
            money=Money,
            date_in=DateIn,
            date_out=DateOut,
            type=Type,
            remark=Remark,
        )

        # json添加数据
        self.taskList.add_task(task)

        # 更新界面
        self.update_table_ui()
        self.update_text(self.ui.MessageLabel, repr(task))

    def finishTodo(self):
        row = self.ui.Table.currentRow()
        if not row == -1:
            getId = self.ui.Table.item(row, 6).text()
            self.update_text(self.ui.MessageLabel, getId)
            task = self.taskList.get_task_by_id(getId)
            print(task)
            print()
            task.set_status("old")
            print(task)
            self.taskList.update_task(task)
        self.update_table_ui()

    def update_table_ui(self):
        self.ui.Table.setRowCount(0)
        self.ui.Table_old.setRowCount(0)
        tableList = self.taskList.get_all_tasks()
        for task in tableList:
            if task.status == "new":
                task.tableAdd(self.ui.Table)
            else:
                task.tableAdd(self.ui.Table_old)

    def update_text(self, object, new_text):
        object.setText(new_text)


app = QApplication([])
main = Main()
main.ui.show()
app.exec()
