from PySide6.QtCore import QDate, Qt
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QAbstractItemView, QApplication, QMessageBox, QFileDialog

from task import Task
from task_list import TaskList


class Main:
    def __init__(self):
        # 从文件中加载UI定义
        self.ui = QUiLoader().load("bill.ui")
        self.updateUI = QUiLoader().load("updateTodo.ui")

        # 设置钩子函数
        self.ui.AddTodoButton.clicked.connect(self.addTodo)
        self.ui.FinishTodoButton.clicked.connect(self.finishTodo)
        self.ui.OutputTodoButton.clicked.connect(self.OutputTodo)
        self.ui.UpdateTodoButton.clicked.connect(self.UpdateTodo)
        self.updateUI.UpdateButton.clicked.connect(self.UpdateTodoMini)

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
        self.updateUI.InDateEdit.setDate(currentDate)
        self.updateUI.InDateEdit.setCalendarPopup(True)
        self.updateUI.OutDateEdit.setDate(currentDate)
        self.updateUI.OutDateEdit.setCalendarPopup(True)

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
        choice = QMessageBox.question(self.ui, "Are you sure", "您确认要执行该操作?")
        if choice == QMessageBox.Yes:
            # 获取选中的目标行索引
            row = self.ui.Table.currentRow()
            if not row == -1:
                # 获取对应的id
                getId = self.ui.Table.item(row, 6).text()
                self.update_text(self.ui.MessageLabel, getId)
                # 获取对应的task对象并更改数据
                task = self.taskList.get_task_by_id(getId)
                task.set_status("old")
                # 更新数据库
                self.taskList.update_task(task)
            self.update_table_ui()
        elif choice == QMessageBox.No:
            print("取消")

    def OutputTodo(self):
        folder_name = QFileDialog.getExistingDirectory(self.ui, "选择你要保存的文件夹", "../")
        if not folder_name == "":
            self.update_text(self.ui.MessageLabel, "保存成功")
            path = f"{folder_name}/output.xlsx"
            # print(path)
            self.taskList.export_json_to_excel(path)

    def UpdateTodo(self):
        row = self.ui.Table.currentRow()
        if not row == -1:
            self.updateUI.show()
            # 获取目标task
            getId = self.ui.Table.item(row, 6).text()
            self.update_text(self.ui.MessageLabel, getId)
            task = self.taskList.get_task_by_id(getId)

            # 回显数据
            self.update_id = task.id
            self.update_status = task.status
            Target = self.updateUI.ObjectEdit.setText(task.target)
            Money = self.updateUI.MoneyEdit.setText(task.money)
            DateIn = self.updateUI.InDateEdit.setDate(QDate.fromString(task.date_in))
            DateOut = self.updateUI.OutDateEdit.setDate(QDate.fromString(task.date_out))
            Type = self.updateUI.TypeEdit.setCurrentText(task.type)
            Remark = self.updateUI.RemarkEdit.setText(task.remark)

            self.taskList.update_task(task)
        else:
            QMessageBox.warning(self.ui, "认真的吗？", "你未选中任何内容")
        self.update_table_ui()

    def UpdateTodoMini(self):
        # 从信息栏中获取信息
        Target = self.updateUI.ObjectEdit.text()
        Money = self.updateUI.MoneyEdit.text()
        DateIn = self.updateUI.InDateEdit.text()
        DateOut = self.updateUI.OutDateEdit.text()
        Type = self.updateUI.TypeEdit.currentText()
        Remark = self.updateUI.RemarkEdit.text()

        # 对信息栏进行判断
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
        
        task.set_id(self.update_id)
        task.set_status(self.update_status)
        self.update_text(self.ui.MessageLabel, repr(task))

        # 更新数据刷新页面
        self.taskList.update_task(task)
        self.update_table_ui()
        self.updateUI.close()

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
