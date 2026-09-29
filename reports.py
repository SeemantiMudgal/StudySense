from subjects import get_subjects
from tasks import get_tasks
from study_sessions import get_sessions


def generate_report():
    subjects = get_subjects()
    tasks = get_tasks()
    sessions = get_sessions()

    total_study_time = sum(session["duration"] for session in sessions)

    completed_tasks = sum(
        1 for task in tasks if task["completed"]
    )

    pending_tasks = len(tasks) - completed_tasks

    subject_hours = {}

    for session in sessions:
        subject = session["subject"]
        subject_hours[subject] = (
            subject_hours.get(subject, 0) + session["duration"]
        )

    most_studied_subject = "None"

    if subject_hours:
        most_studied_subject = max(
            subject_hours,
            key=subject_hours.get
        )

    productivity = 0

    if tasks:
        productivity = (completed_tasks / len(tasks)) * 100

    return {
        "total_study_time": total_study_time,
        "completed_tasks": completed_tasks,
        "pending_tasks": pending_tasks,
        "most_studied_subject": most_studied_subject,
        "subject_hours": subject_hours,
        "productivity": round(productivity, 2)
    }