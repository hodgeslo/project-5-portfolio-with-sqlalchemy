from flask import render_template, url_for, request, redirect, flash
from models import app, Project, db, add_csv
import datetime

ROWS_PER_PAGE = 5
MY_NAME = "Lonnie Hodges"


def page_results():
    page = request.args.get('page', 1, type=int)
    projects = Project.query.paginate(page=page, per_page=ROWS_PER_PAGE)
    return projects


@app.route('/')
def index():
    projects = page_results()
    return render_template('index.html', projects=projects, my_name=MY_NAME)


@app.route('/about')
def about():
    projects = page_results()
    return render_template('about.html', projects=projects, my_name=MY_NAME)


@app.route('/contact')
def contact():
    projects = page_results()
    return render_template('contact.html', projects=projects, my_name=MY_NAME)


@app.route('/skills')
def skills():
    projects = page_results()
    return render_template('skills.html', projects=projects, my_name=MY_NAME)


@app.route('/project/<int:id>')
def detail_project(id):
    get_project = Project.query.get_or_404(id)
    projects = page_results()
    return render_template('detail.html', get_project=get_project, projects=projects, my_name=MY_NAME)


@app.route('/project/new', methods=['GET', 'POST'])
def add_project():
    projects = page_results()
    if request.form:
        print(request.form)
        new_project = Project(
            title=request.form['title'],
            date_created=datetime.datetime.strptime(request.form['date'], '%Y-%m-%d'),
            description=request.form['desc'],
            skills=request.form['skills'],
            repo_link=request.form['github']
        )
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('addproject.html', projects=projects, my_name=MY_NAME)


@app.route('/project/<int:id>/edit', methods=['GET', 'POST'])
def edit_project(id):
    get_project = Project.query.get_or_404(id)
    projects = page_results()
    if request.form:
        print(request.form)
        get_project.title = request.form['title']
        get_project.date_created = datetime.datetime.strptime(request.form['date'], '%Y-%m-%d')
        get_project.description = request.form['desc']
        get_project.skills = request.form['skills']
        get_project.repo_link = request.form['github']

        db.session.commit()

        return redirect(url_for('index'))
    return render_template('projectform.html', get_project=get_project, projects=projects, my_name=MY_NAME)


@app.route('/project/<int:id>/delete', methods=['GET', 'POST'])
def delete_project(id):
    # projects = page_results()
    get_project = Project.query.get_or_404(id)
    db.session.delete(get_project)
    db.session.commit()
    flash('Project has been deleted from database.')
    return redirect(url_for('index'))


@app.errorhandler(404)
def not_found(error):
    projects = page_results()
    return render_template('404.html', msg=error, projects=projects, my_name=MY_NAME), 404


if __name__ == '__main__':
    with app.app_context():
        add_csv()
    app.run(debug=True, port=9000)
