from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime
from os import path
import csv

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


def add_csv():
    csv_file_to_import = 'projects.csv'
    if path.isfile(csv_file_to_import):
        db.create_all()
        with open(csv_file_to_import) as csvfile:
            data = csv.reader(csvfile, delimiter='\t')
            next(data)  # <<< skip header row
            for row in data:
                product_in_db = db.session.query(Project).filter(Project.title == row[0]).one_or_none()
                if product_in_db is None:
                    title = row[0]
                    date_created = datetime.datetime.strptime(row[1], '%Y-%m-%d')
                    description = row[2]
                    skills = row[3]
                    repo_link = row[4]
                    new_project = Project(title=title, date_created=date_created,
                                          description=description, skills=skills, repo_link=repo_link)
                    db.session.add(new_project)
            db.session.commit()
        return True
    else:
        print(f"CSV to import not found.")
        print(f"Quitting application...")
        return False


