class Task:
    def __init__(self, title, description, deadline):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Виконано" if self.completed else "Не виконано"

        return (
            f"Назва: {self.title}\n"
            f"Опис: {self.description}\n"
            f"Дедлайн: {self.deadline}\n"
            f"Стан: {status}"
        )


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Завдання '{task.title}' додано.")

    def delete_task(self, title):
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                print(f"Завдання '{title}' видалено.")
                return

        print(f"Завдання '{title}' не знайдено.")

    def complete_task(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_completed()
                print(f"Завдання '{title}' позначено як виконане.")
                return

        print(f"Завдання '{title}' не знайдено.")

    def show_tasks(self):
        if not self.tasks:
            print("Список завдань порожній.")
            return

        print("\n--- Список завдань ---")

        for i, task in enumerate(self.tasks, start=1):
            print(f"\nЗавдання №{i}")
            print(task)


manager = TaskManager()

task1 = Task(
    "Вивчити Python",
    "Опрацювати класи та об'єкти",
    "05.10.2026"
)

task2 = Task(
    "Зробити домашнє завдання",
    "Виконати завдання з програмування",
    "03.10.2026"
)

manager.add_task(task1)
manager.add_task(task2)

manager.show_tasks()

manager.complete_task("Вивчити Python")

manager.show_tasks()

manager.delete_task("Зробити домашнє завдання")

manager.show_tasks()