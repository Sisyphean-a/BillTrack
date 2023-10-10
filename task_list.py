import json
import os
import time

from task import Task
import xlsxwriter


class TaskList:
    def __init__(self):
        self.tasks = []

        user_dir = os.path.expanduser("~")
        # 如果用户目录不存在目标文件夹则创建一个
        if not os.path.exists(os.path.join(user_dir, "WineAndBill")):
            os.makedirs(os.path.join(user_dir, "WineAndBill"))

        # 获取目标文件夹路径
        self.load_path = os.path.join(user_dir, "WineAndBill", "list_data.json")
        if not os.path.exists(self.load_path):
            data = []
            with open(self.load_path, "w") as f:
                json.dump(data, f)

        # 从文件中加载数据
        with open(self.load_path, "r", encoding="utf-8") as file:
            self.tasks = json.load(file)

    def add_task(self, task):
        self.tasks.append(self.to_json(task))
        self.save()

    def update_task(self, task):
        for i, t in enumerate(self.tasks):
            if task.id == t["id"]:
                # 更新任务
                t["target"] = task.target
                t["money"] = task.money
                t["date_in"] = task.date_in
                t["date_out"] = task.date_out
                t["type"] = task.type
                t["remark"] = task.remark
                t["status"] = task.status
                self.tasks[i] = t
                self.save()
                return True
        return False

    def save(self):
        with open(self.load_path, "w") as f:
            json.dump(self.tasks, f)

    def get_all_tasks(self):
        tasks = []
        for task_json in self.tasks:
            task = Task(
                task_json["target"],
                task_json["money"],
                task_json["date_in"],
                task_json["date_out"],
                task_json["type"],
                task_json["remark"],
            )
            task.set_status(task_json["status"])
            task.set_id(task_json["id"])
            tasks.append(task)
        return tasks

    def get_task_by_id(self, id):
        for task_json in self.tasks:
            if task_json["id"] == id:
                task = Task(
                    task_json["target"],
                    task_json["money"],
                    task_json["date_in"],
                    task_json["date_out"],
                    task_json["type"],
                    task_json["remark"],
                )
                task.set_status(task_json["status"])
                task.set_id(task_json["id"])
                return task
        return None

    def get_new_task(self,id):
        task = self.get_task_by_id(id)
        # time.sleep(0.0001)
        # current_milli_time = lambda: int(round(time.time() * 1000))
        # task.set_id = str(current_milli_time())
        task.new_time()    
        return task

    def to_json(self, task):
        return {
            "id": task.id,
            "target": task.target,
            "money": task.money,
            "date_in": task.date_in,
            "date_out": task.date_out,
            "type": task.type,
            "remark": task.remark,
            "status": task.status,
        }

    def export_json_to_excel(self, excel_file_name):
        # 将json数据转换为二维数组
        data = [item for item in self.tasks]
        # 获取表头
        headers = data[0].keys()
        # 创建excel文件
        workbook = xlsxwriter.Workbook(excel_file_name)
        # 创建工作表
        worksheet = workbook.add_worksheet()
        # 设置表头
        for i, header in enumerate(headers):
            worksheet.write(0, i, header)
        # 写入数据
        for i, row in enumerate(data):
            for j, value in enumerate(row.values()):
                worksheet.write(i + 1, j, value)
        # 保存excel文件
        workbook.close()


if __name__ == "__main__":
    task_list = TaskList()

    task_list.export_json_to_excel("output.xlsx")

    # 添加任务
    # task_list.add_task(Task("学习 Python", "1000", "2023-08-01", "2023-08-31", "学习"))
    # task_list.add_task(Task("健身", "2000", "2023-08-01", "2023-08-31", "健身"))
    # task_list.add_task(Task("旅行", "3000", "2023-08-01", "2023-08-31", "旅行"))

    # # 获取所有任务
    # print(task_list.get_all_tasks())
    # print("\n\n")

    # # 获取指定任务
    # task = task_list.get_task_by_id("1696297727776")
    # # 修改数据
    # task.set_status("old")
    # # 更新数据
    # task_list.update_task(task)
    # print(task)
