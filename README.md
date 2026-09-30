# StudySense

StudySense is a command-line Python application designed to help students organize their study activities in one place.

It allows users to manage subjects, create study tasks, record study sessions, and view a productivity report.

## Features

- Add and view subjects
- Set study targets for subjects
- Track study hours for each subject
- Add study tasks with deadlines and priorities
- View pending and completed tasks
- Mark tasks as completed
- Delete tasks
- Record study sessions
- View recorded study sessions
- Generate a productivity report
- Store data locally using JSON files
- Validate user input
- Run completely through the command line

## Project Structure

```text
StudySense/
│
├── data/
│   ├── subjects.json
│   ├── tasks.json
│   └── sessions.json
│
├── tests/
│   └── test_studysense.py
│
├── main.py
├── subjects.py
├── tasks.py
├── study_sessions.py
├── reports.py
├── storage.py
├── validators.py
├── README.md
├── statement.md
└── .gitignore
## Technologies / Tools Used

- Python 3
- JSON
- Git and GitHub
- Visual Studio Code
## Installation and Running

1. Clone the repository.

2. Open the project folder in a terminal.

3. Make sure Python 3 is installed.

4. Run the application using:

```bash
python3 main.py
## Testing

The project includes automated tests in the `tests` folder.

Install pytest:

```bash
python3 -m pip install pytest
python3 -m pytest