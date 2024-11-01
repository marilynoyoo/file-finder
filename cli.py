import click
from sqlalchemy.orm import sessionmaker
from models import User, Task, Category, Base
from database import engine

Session = sessionmaker(bind=engine)

@click.group()
def cli():
    pass

@cli.command()
@click.argument('title')
@click.argument('description')
def add_task(title, description):
    session = Session()
    new_task = Task(title=title, description=description)
    session.add(new_task)
    session.commit()
    click.echo(f'Task "{title}" added!')


