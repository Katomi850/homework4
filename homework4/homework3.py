import random

class Task:
    def __init__(self, name, deadline):
        self.name = name
        self.deadline = deadline
        self.done = False

    def complete(self):
        self.done = True

    def __str__(self):
        status = "+" if self.done else "-"
        return f"{status} {self.name} (до {self.deadline})"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, name, deadline):
        self.tasks.append(Task(name, deadline))

    def show_tasks(self):
        print("Завдання:")
        for task in self.tasks:
            print(task)

    def get_unfinished(self):
        return [task for task in self.tasks if not task.done]

    def live(self, day, energy):
        print(f"\n========== День {day} ==========")
        self.show_tasks()
        if energy < 20:
            print("Мало енергії, відпочивай")
            return energy + 10
        unfinished = self.get_unfinished()
        if unfinished:
            task = random.choice(unfinished)
            print(f"Виконую: {task.name}")
            task.complete()
            return energy - 10
        else:
            print("Нема завдань, відпочивай")
            return energy + 5


manager = TaskManager()
manager.add_task("Вивчити Python", "2025-05-20")
manager.add_task("Зробити домашку", "2025-05-21")

energy = 50
for day in range(1, 6):
    energy = manager.live(day, energy)
