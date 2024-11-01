# Task Manager CLI

## Description
Task Manager CLI is a command-line application that helps users manage their tasks efficiently. Users can create, view, update, and delete tasks while keeping everything organized. The application uses SQLAlchemy for ORM (Object-Relational Mapping) and SQLite as the database backend.

## Installation Instructions

1. **Clone the Repository**:
   ```bash
   git clone <git@github.com:marilynoyoo/file-finder.git>
   cd file-finder

2. **Set Up the Virtual Environment**: Ensure you have Pipenv installed. If not, you can install it using:
pip install pipenv

3. **Install Dependencies**: 
Run the following command to install the required packages:
pipenv install

4. **Set Up the Database**: 
Create the SQLite database and tables by running:
pipenv run python database.py

# Usage Instructions
# Running the Application
To start the CLI application, run:
pipenv run python main.py

# Available Commands
**Add a Task**: 
To add a new task, use:
pipenv run python main.py add-task "Task Title" "Task Description"

Replace "Task Title" and "Task Description" with your task details.

**List All Tasks**: 
To view all tasks, use:
pipenv run python main.py list-tasks

# Example
1. **Add a task**:
pipenv run python main.py add-task "Finish Project" "Complete the CLI project by the deadline."

2. **List tasks**:
pipenv run python main.py list-tasks

# Notes
Ensure you run the commands from within the project directory.
You can enhance the CLI by adding more commands like updating or deleting tasks.

# Contributing
Feel free to submit issues and pull requests. Contributions are welcome!

# License
This project is open-source and available under the MIT License.

## Prepared By
This project was developed by.
Name : Marilyn akinyi oyoo
Email address : marilynakinyi@gmail.com
Feel free to reach out for questions or suggestions.

## Acknowledgements
- Thanks to Moringa School and Flatiron School, such as:
  - [SQLAlchemy](https://www.sqlalchemy.org/) for ORM capabilities.
  - [Click](https://click.palletsprojects.com/) for creating the command-line interface.
- Special thanks to Julius Mwangi and Ian  who provided guidance and support throughout the project.



### How to Use This README

- Replace `<repository-url>` with the actual URL of your project repository.
- Adjust the License section if you choose a different license.
- You can add more sections if you expand the functionality, such as features, examples of more complex commands, or a changelog.

This README provides a comprehensive guide for users to understand your project and get started quickly. Let me know if you need any modifications or additional information!



