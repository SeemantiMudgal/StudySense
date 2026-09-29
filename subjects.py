from storage import load_data, save_data

FILE_NAME = "subjects.json"


def add_subject(name, target_hours):
    subjects = load_data(FILE_NAME)

    subject = {
        "name": name,
        "target_hours": target_hours,
        "studied_hours": 0
    }

    subjects.append(subject)
    save_data(FILE_NAME, subjects)


def get_subjects():
    return load_data(FILE_NAME)


def update_study_hours(name, hours):
    subjects = load_data(FILE_NAME)

    for subject in subjects:
        if subject["name"].lower() == name.lower():
            subject["studied_hours"] += hours
            break

    save_data(FILE_NAME, subjects)