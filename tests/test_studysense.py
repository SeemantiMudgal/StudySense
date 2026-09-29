from subjects import add_subject, get_subjects
from tasks import add_task, get_tasks
from study_sessions import add_session, get_sessions


def test_add_subject():
    add_subject("Test Python", 10)

    subjects = get_subjects()

    assert any(
        subject["name"] == "Test Python"
        for subject in subjects
    )


def test_add_task():
    add_task(
        "Test Task",
        "Test Python",
        "30-09-2026",
        "High"
    )

    tasks = get_tasks()

    assert any(
        task["title"] == "Test Task"
        for task in tasks
    )


def test_add_session():
    add_session(
        "Test Python",
        "Testing",
        30,
        "29-09-2026"
    )

    sessions = get_sessions()

    assert any(
        session["topic"] == "Testing"
        for session in sessions
    )