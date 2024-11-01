import click
from sqlalchemy.orm import Session
from database.db import setup_database, teardown_database, Session
from models.task import Task
from models.user import User

@click.group()
def cli():
    """CLI for managing tasks."""
    pass

@cli.command()
@click.argument('name')
@click.argument('email')
def add_user(name, email):
    """Add a new user."""
    session = Session()
    user = User(name=name, email=email)
    session.add(user)
    session.commit()
    click.echo(f'User {name} added!')
    session.close()

@cli.command()
@click.argument('title')
@click.argument('description')
@click.argument('user_id', type=int)
def add_task(title, description, user_id):
    """Add a new task."""
    session = Session()
    task = Task(title=title, description=description, user_id=user_id)
    session.add(task)
    session.commit()
    click.echo(f'Task "{title}" added!')
    session.close()

@cli.command()
def setup():
    """Set up the database."""
    setup_database()
    click.echo("Database setup complete.")

@cli.command()
def teardown():
    """Teardown the database."""
    teardown_database()
    click.echo("Database teardown complete.")

if __name__ == '__main__':
    cli()
