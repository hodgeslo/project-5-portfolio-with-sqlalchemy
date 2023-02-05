from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///projects.db"
db = SQLAlchemy(app)


class Project(db.Model):
    __tablename__ = 'project'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column('Title', db.String())
    date_created = db.Column('Date Created', db.DateTime,
                             default=datetime.datetime.now)  # .now instead of .now(). We want to run every time a record is created
    description = db.Column('Description', db.Text)
    skills = db.Column('Skills', db.Text)
    repo_link = db.Column('Repo Link', db.Text)


def __repr__(self):
    return f'''
    <Project (Title: {self.title}
    Date Created: {self.date_created}
    Description: {self.description}
    Skills: {self.skills}
    Repo Link: {self.repo_link}
    '''
