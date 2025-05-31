class Task:
    def __init__(self, title, description, deadline):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.completed = False

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def delete_task(self, task_title):
        for task in self.tasks:
            if task.title == task_title:
                self.tasks.remove(task)

    def mark_task_completed(self, task_title):
        for task in self.tasks:
            if task.title == task_title:
                task.completed = True

    def show_tasks(self):
        if not self.tasks:
            print("Немає завдань.")
        for task in self.tasks:
            print("Назва:", task.title)
            print("Опис:", task.description)
            print("Дедлайн:", task.deadline)
            print("Виконано:" if task.completed else "Не виконано")

def main():
    manager = TaskManager()

    while True:
        print("1 - Додати завдання")
        print("2 - Видалити завдання")
        print("3 - Позначити як виконане")
        print("4 - Показати всі завдання")
        print("5 - Вийти")

        choice = input("Оберіть дію: ")

        if choice == "1":
            title = input("Введіть назву: ")
            description = input("Введіть опис: ")
            deadline = input("Введіть дедлайн: ")
            task = Task(title, description, deadline)
            manager.add_task(task)
            print("Завдання додано.")

        elif choice == "2":
            title = input("Введіть назву завдання для видалення: ")
            if manager.delete_task(title):
                print("Завдання видалено.")
            else:
                print("Завдання не знайдено.")

        elif choice == "3":
            title = input("Введіть назву завдання для позначення як виконане: ")
            if manager.mark_task_completed(title):
                print("Завдання позначено як виконане.")
            else:
                print("Завдання не знайдено.")

        elif choice == "4":
            manager.show_tasks()

        elif choice == "5":
            print("Вихід з програми.")

        else:
            print("Невірна дія, спробуйте ще раз.")


if __name__ == "__main__":
    main()