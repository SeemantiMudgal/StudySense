# StudySense

## Overview

StudySense is a command-line Python application that helps students organize study tasks, record study sessions, monitor subject-wise progress, and generate productivity reports.

The application stores data locally using JSON files and provides a simple menu-driven interface for managing study activities.

## Features

- Add and manage subjects
- Set study targets for subjects
- Add, view, complete, and delete study tasks
- Set task deadlines and priorities
- Record study sessions
- Track subject-wise study time
- Generate productivity reports
- Store data locally using JSON
- Validate user input
- Run automated tests

## Technologies / Tools Used

- Python 3
- JSON
- Git and GitHub
- Visual Studio Code
- pytest

## Project Structure

```text
StudySense/
├── main.py
├── subjects.py
├── tasks.py
├── study_sessions.py
├── reports.py
├── storage.py
├── validators.py
├── data/
│   ├── subjects.json
│   ├── tasks.json
│   └── sessions.json
├── tests/
│   └── test_studysense.py
├── README.md
└── statement.md