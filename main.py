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

        # 设置表格相关属性，不可编辑、整行选中、排序功能
        self.ui.Table.horizontalHeader().setStretchLastSection(True)
        self.ui.Table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.Table.setSortingEnabled(True)
        self.ui.Table_old.horizontalHeader().setStretchLastSection(True)
        self.ui.Table_old.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.Table_old.setSortingEnabled(True)

        # 设置初始化时间为当前时间
        currentDate = QDate.currentDate()
        self.ui.InDateEdit.setDate(currentDate)
        self.ui.InDateEdit.setCalendarPopup(True)
        self.ui.OutDateEdit.setDate(currentDate)
        self.ui.OutDateEdit.setCalendarPopup(True)

        # 初始化表格
        self.taskList = TaskList()
        tableList = self.taskList.get_all_tasks()
        for task in tableList:
            task.tableAdd(self.ui.Table)

    def addTodo(self):
        Target = self.ui.ObjectEdit.text()
        Money = self.ui.MoneyEdit.text()
        DateIn = self.ui.InDateEdit.text()
        DateOut = self.ui.OutDateEdit.text()
        Type = self.ui.TypeEdit.currentText()
        Remark = self.ui.RemarkEdit.text()

        if Target == "" or Money == "" or DateIn == "" or DateOut == "" or Type == "":
            self.update_text(self.ui.MessageLabel, "账单消息不完整\n添加失败")
            return

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

    def update_table_ui(self):
        tableList = self.taskList.get_all_tasks()
        for task in tableList:
            task.tableAdd(self.ui.Table)

    def update_text(self, object, new_text):
        object.setText(new_text)


app = QApplication([])
main = Main()
main.ui.show()
app.exec()
