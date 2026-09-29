from storage import load_data, save_data

FILE_NAME = "tasks.json"


def add_task(title, subject, deadline, priority):
    tasks = load_data(FILE_NAME)

    task = {
        "title": title,
        "subject": subject,
        "deadline": deadline,
        "priority": priority,
        "completed": False
    }

    tasks.append(task)
    save_data(FILE_NAME, tasks)


def get_tasks():
    return load_data(FILE_NAME)


def complete_task(title):
    tasks = load_data(FILE_NAME)

    for task in tasks:
        if task["title"].lower() == title.lower():
            task["completed"] = True
            break

    save_data(FILE_NAME, tasks)


def delete_task(title):
    tasks = load_data(FILE_NAME)

    tasks = [
        task for task in tasks
        if task["title"].lower() != title.lower()
    ]

    save_data(FILE_NAME, tasks)