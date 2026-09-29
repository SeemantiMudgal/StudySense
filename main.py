from subjects import add_subject, get_subjects, update_study_hours
from tasks import add_task, get_tasks, complete_task, delete_task
from study_sessions import add_session, get_sessions
from reports import generate_report
from validators import (
    get_non_empty_input,
    get_positive_number,
    get_priority
)


def show_subjects():
    subjects = get_subjects()

    if not subjects:
        print("\nNo subjects added yet.")
        return

    print("\n--- Subjects ---")

    for subject in subjects:
        print(
            f"{subject['name']} | "
            f"Target: {subject['target_hours']} hrs | "
            f"Studied: {subject['studied_hours']:.2f} hrs"
        )


def show_tasks():
    tasks = get_tasks()

    if not tasks:
        print("\nNo tasks added yet.")
        return

    print("\n--- Tasks ---")

    for task in tasks:
        status = "Completed" if task["completed"] else "Pending"

        print(
            f"{task['title']} | "
            f"{task['subject']} | "
            f"Deadline: {task['deadline']} | "
            f"Priority: {task['priority']} | "
            f"{status}"
        )


def show_sessions():
    sessions = get_sessions()

    if not sessions:
        print("\nNo study sessions recorded yet.")
        return

    print("\n--- Study Sessions ---")

    for session in sessions:
        print(
            f"{session['date']} | "
            f"{session['subject']} | "
            f"{session['topic']} | "
            f"{session['duration']} minutes"
        )


def show_report():
    report = generate_report()

    print("\n--- Productivity Report ---")
    print(f"Total study time: {report['total_study_time']} minutes")
    print(f"Completed tasks: {report['completed_tasks']}")
    print(f"Pending tasks: {report['pending_tasks']}")
    print(f"Most studied subject: {report['most_studied_subject']}")
    print(f"Productivity: {report['productivity']}%")

    print("\nSubject-wise study time:")

    if report["subject_hours"]:
        for subject, minutes in report["subject_hours"].items():
            print(f"{subject}: {minutes} minutes")
    else:
        print("No study sessions recorded.")


def main():
    while True:
        print("\n========== StudySense ==========")
        print("1. Add Subject")
        print("2. View Subjects")
        print("3. Add Study Task")
        print("4. View Tasks")
        print("5. Complete Task")
        print("6. Delete Task")
        print("7. Record Study Session")
        print("8. View Study Sessions")
        print("9. View Productivity Report")
        print("0. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            name = get_non_empty_input("Subject name: ")
            target = get_positive_number("Target study hours: ")

            add_subject(name, target)
            print("Subject added successfully.")

        elif choice == "2":
            show_subjects()

        elif choice == "3":
            title = get_non_empty_input("Task title: ")
            subject = get_non_empty_input("Subject: ")
            deadline = get_non_empty_input("Deadline: ")
            priority = get_priority()

            add_task(title, subject, deadline, priority)
            print("Task added successfully.")

        elif choice == "4":
            show_tasks()

        elif choice == "5":
            title = get_non_empty_input("Task title to complete: ")

            complete_task(title)
            print("Task marked as completed.")

        elif choice == "6":
            title = get_non_empty_input("Task title to delete: ")

            delete_task(title)
            print("Task deleted successfully.")

        elif choice == "7":
            subject = get_non_empty_input("Subject: ")
            topic = get_non_empty_input("Topic studied: ")
            duration = get_positive_number("Duration (minutes): ")
            date = get_non_empty_input("Date (DD-MM-YYYY): ")

            add_session(subject, topic, duration, date)
            update_study_hours(subject, duration / 60)

            print("Study session recorded successfully.")

        elif choice == "8":
            show_sessions()

        elif choice == "9":
            show_report()

        elif choice == "0":
            print("\nThank you for using StudySense!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()