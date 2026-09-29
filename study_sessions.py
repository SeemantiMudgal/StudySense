from storage import load_data, save_data

FILE_NAME = "sessions.json"


def add_session(subject, topic, duration, date):
    sessions = load_data(FILE_NAME)

    session = {
        "subject": subject,
        "topic": topic,
        "duration": duration,
        "date": date
    }

    sessions.append(session)
    save_data(FILE_NAME, sessions)


def get_sessions():
    return load_data(FILE_NAME)