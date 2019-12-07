"""Hackbright Project Tracker.

A front-end for a database that allows users to work with students, class
projects, and the grades students receive in class projects.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()


def connect_to_db(app):
    """Connect the database to our Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///hackbright'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


def get_student_by_github(github):
    """Given a GitHub account name, print info about the matching student."""

    QUERY = """
        SELECT first_name, last_name, github
        FROM students
        WHERE github = :github
        """

    db_cursor = db.session.execute(QUERY, {'github': github})
    row = db_cursor.fetchone()
    print("Student: {} {}\nGitHub account: {}".format(row[0], row[1], row[2]))


def make_new_student(first_name, last_name, github):
    """Add a new student and print confirmation.

    Given a first name, last name, and GitHub account, add student to the
    database and print a confirmation message.
    """
    QUERY = """
        INSERT INTO students (first_name, last_name, github)
            VALUES (:first_name, :last_name, :github)
        """

    db.session.execute(QUERY, {'first_name': first_name,
                               'last_name': last_name,
                               'github': github
                               })
    db.session.commit()
    print(f"Student: {first_name} {last_name}\nGitHub account: {github} added.")


def make_new_project(title, max_grade, description):
    """Add a new project and print confirmation.

    Given a title, description, and max_grande,add project to the
    database and print a confirmation message.
    """
    QUERY = """
        INSERT INTO projects (title, max_grade, description)
            VALUES (:title, :max_grade, :description)
        """

    db.session.execute(QUERY, {'title': title,
                               'max_grade': max_grade,
                               'description': description,
                               })
    db.session.commit()
    print(f"Project: {title} was successfully added.")


def get_project_by_title(title):
    """Given a project title, print information about the project."""
    QUERY = """
        SELECT title, description, max_grade
        FROM projects
        WHERE title = :title
        """

    db_cursor = db.session.execute(QUERY, {'title': title})
    row = db_cursor.fetchone()
    print(f"Title: {row[0]}\nDescription: {row[1]}\nMax Grade: {row[2]}")


def get_grade_by_github_title(github, title):
    """Print grade student received for a project."""
    
    QUERY = """
        SELECT grade
        FROM grades
        WHERE student_github = :github AND project_title = :title
        """

    db_cursor = db.session.execute(QUERY, {'github': github, 'title': title})
    row = db_cursor.fetchone()
    print(f"{github} received {row[0]} for project {title}.")


def get_all_grades_for_student(first_name, last_name):
    """Print grade for each project given student name."""

    QUERY = """
        SELECT project_title, grade
        FROM grades
        LEFT JOIN students
        ON grades.student_github = students.github
        WHERE first_name = :first_name
        AND last_name = :last_name
        """

    db_cursor = db.session.execute(QUERY, {'first_name': first_name,
                                           'last_name': last_name})
    rows = db_cursor.fetchall()
    for i in range(len(rows)):
        print(f"{rows[i][0]}: {rows[i][1]}")


def assign_grade(github, title, grade):
    """Assign a student a grade on an assignment and print a confirmation."""
    QUERY = """
        INSERT INTO grades (student_github, project_title, grade)
        VALUES (:github, :title, :grade)
        """

    db.session.execute(QUERY, {'github': github, 'title': title, 'grade': grade})
    db.session.commit()
    print(f"Grade assigned for project {title} to {github}.")


def handle_input():
    """Main loop.

    Repeatedly prompt for commands, performing them, until 'quit' is received
    as a command.
    """

    def handle_errors(args):
        if args != req_args:
            print("Invalid number of arguments, please try again!")

    command = None

    while command != "quit":
        input_string = input("HBA Database> ")
        tokens = input_string.split()
        command = tokens[0]
        args = tokens[1:]

        if command == "student":
            req_args = 1
            handle_errors(args)
            github = args[0]
            get_student_by_github(github)

        elif command == "new_student":
            req_args = 3
            handle_errors(args)
            first_name, last_name, github = args  # unpack!
            make_new_student(first_name, last_name, github)

        elif command == "project":
            req_args = 1
            handle_errors(args)
            title = args[0]
            get_project_by_title(title)

        elif command == "grade":
            req_args = 2
            handle_errors(args)
            github, title = args
            get_grade_by_github_title(github, title)

        elif command == "assign_grade":
            req_args = 3
            handle_errors(args)
            github, title, grade = args
            assign_grade(github, title, grade)

        elif command == "add_project":
            req_args >= 3
            handle_errors(args)
            title, max_grade = args[:2]
            description = (' ').join(args[2:])
            make_new_project(title, max_grade, description)

        elif command == "get_grades":
            req_args = 2
            handle_errors(args)
            first_name, last_name = args
            get_all_grades_for_student(first_name, last_name)

        else:
            if command != "quit":
                print("Invalid Entry. Try again.")


if __name__ == "__main__":
    connect_to_db(app)

    # handle_input()

    # To be tidy, we close our database connection -- though,
    # since this is where our program ends, we'd quit anyway.

    db.session.close()
