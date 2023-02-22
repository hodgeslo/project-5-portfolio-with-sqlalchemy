from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
import csv
import datetime

app = Flask(__name__)
app.secret_key = b'>D9c8Ln2X)Eo$Tox2}rU.'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///projects.db"
db = SQLAlchemy(app)


class Project(db.Model):
    __tablename__ = 'project'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column('Title', db.String())
    date_created = db.Column('Date Created', db.Date,
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


def add_csv():
    csv_file_to_import = 'projects.txt'
    if path.isfile(csv_file_to_import):
        db.create_all()
        with open(csv_file_to_import) as csvfile:
            data = csv.DictReader(csvfile, delimiter='\t')
            for row in data:
                product_in_db = db.session.query(Project).filter(Project.title == row['title']).one_or_none()
                if product_in_db is None:
                    title = row['title']
                    date_created = datetime.datetime.strptime(row['date_created'], '%m/%d/%Y')
                    description = row['description']
                    skills = row['skills']
                    repo_link = row['repo_link']
                    new_project = Project(title=title, date_created=date_created,
                                          description=description, skills=skills, repo_link=repo_link)
                    db.session.add(new_project)
            db.session.commit()
        return True
    else:
        print(f"CSV to import not found.")
        print(f"Quitting application...")
        return False
