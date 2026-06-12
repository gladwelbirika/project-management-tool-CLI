# TaskTrack CLI

A Python-based Command-Line Interface (CLI) application for managing users, projects, and tasks. The system demonstrates object-oriented programming, file persistence, and CLI interaction using argparse.

## Features

- Create and manage users
- Assign multiple projects to users
- Add multiple tasks to projects
- Mark tasks as complete
- View users, projects, and tasks
- Persistent data storage using JSON files
- Modular object-oriented design
- Unit testing with pytest

## Project Structure

models/        # Core classes (Person, User, Project, Task)
services/      # Business logic (ProjectManager)
utils/         # File storage (JSON load/save)
tests/         # Unit tests using pytest
data/          # Local JSON database
main.py        # CLI entry point

## Installation

Clone the repository:
git clone <your-repo-url>
cd project-management-tool-CLI

Create virtual environment:
python3 -m venv venv
source venv/bin/activate

Install dependencies:
pip install -r requirements.txt

## Usage

Add user:
python main.py add-user --name "Alex" --email "alex@email.com"

Add project:
python main.py add-project --user "Alex" --title "CLI Tool" --description "Build CLI system"

Add task:
python main.py add-task --user "Alex" --project "CLI Tool" --title "Implement CLI"

Complete task:
python main.py complete-task --user "Alex" --project "CLI Tool" --title "Implement CLI"

List users:
python main.py list-users

## Testing

Run tests:
python -m pytest

## Dependencies

Python 3.10+
pytest

Install:
pip install pytest

## Data Storage

All data is stored in:
data/database.json

## Known Limitations

- User and project names must match exactly
- No authentication system
- CLI is case-sensitive
- Uses JSON file storage instead of a database

## Design Overview

Person → User → Project → Task

Relationships:
- One User → Many Projects
- One Project → Many Tasks

## Author

TaskTrack CLI – Python OOP Summative Project