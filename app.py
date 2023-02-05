from flask import render_template, url_for, request, redirect
from models import app


@app.route('/')
def index():
    return render_template('index.html')


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
    app.run(debug=True, port=9000)
