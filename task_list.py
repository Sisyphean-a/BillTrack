import json
import os

from task import Task


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
            tasks.append(task)
        return tasks

    def get_task_by_id(self, id):
        for task in self.tasks:
            if task.id == id:
                return task
        return None

    def to_json(self, task):
        return {
            "target": task.target,
            "money": task.money,
            "date_in": task.date_in,
            "date_out": task.date_out,
            "type": task.type,
            "remark": task.remark,
        }


if __name__ == "__main__":
    task_list = TaskList()

    # 添加任务
    task_list.add_task(Task("学习 Python", "1000", "2023-08-01", "2023-08-31", "学习"))
    task_list.add_task(Task("健身", "2000", "2023-08-01", "2023-08-31", "健身"))
    task_list.add_task(Task("旅行", "3000", "2023-08-01", "2023-08-31", "旅行"))

    # 获取所有任务
    print(task_list.get_all_tasks())

    # 获取指定任务
    # print(task_list.get_task_by_id(1))

    # 保存数据
    # task_list.save()
