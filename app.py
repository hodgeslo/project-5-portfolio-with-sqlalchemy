from flask import render_template, url_for, request, redirect
from models import app, Project, db, add_csv


@app.route('/')
def index():
    projects = Project.query.all()
    return render_template('index.html', projects=projects)


@app.route('/projects/')
def detail_project():
    return render_template('detail.html')


@app.route('/projects/new', methods=['GET', 'POST'])
def new_project():
    return render_template('index.html')


@app.route('/projects/<id>/edit', methods=['GET', 'POST'])
def edit_project(id):
    return render_template('index.html')


@app.route('/projects/<id>/delete', methods=['GET', 'POST'])
def delete_project(id):
    return render_template('index.html')


if __name__ == '__main__':
    with app.app_context():
        add_csv()
    app.run(debug=True, port=9000)
