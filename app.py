from flask import render_template, url_for, request, redirect
from models import app, Project, db, add_csv
import datetime


@app.route('/')
def index():
    projects = Project.query.all()
    nav_projects = Project.query.limit(4)
    page = db.paginate(db.select(Project))
    return render_template('index.html', projects=projects, nav_projects=nav_projects, page=page)


@app.route('/about')
def about():
    projects = Project.query.all()
    nav_projects = Project.query.limit(4)
    return render_template('about.html', projects=projects, nav_projects=nav_projects)


@app.route('/contact')
def contact():
    projects = Project.query.all()
    nav_projects = Project.query.limit(4)
    return render_template('contact.html', projects=projects, nav_projects=nav_projects)


@app.route('/skills')
def skills():
    projects = Project.query.all()
    nav_projects = Project.query.limit(4)
    return render_template('skills.html', projects=projects, nav_projects=nav_projects)


@app.route('/project/<id>')
def detail_project(id):
    get_project = Project.query.get_or_404(id)
    nav_projects = Project.query.limit(4)
    return render_template('detail.html', get_project=get_project, nav_projects=nav_projects)


@app.route('/project/new', methods=['GET', 'POST'])
def add_project():
    nav_projects = Project.query.limit(4)
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
    return render_template('addproject.html', nav_projects=nav_projects)


@app.route('/project/<id>/edit', methods=['GET', 'POST'])
def edit_project(id):
    get_project = Project.query.get_or_404(id)
    nav_projects = Project.query.limit(4)
    return render_template('projectform.html', get_project=get_project, nav_projects=nav_projects)


@app.route('/project/<id>/delete', methods=['GET', 'POST'])
def delete_project(id):
    return render_template('index.html')


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', msg=error), 404


if __name__ == '__main__':
    with app.app_context():
        add_csv()
    app.run(debug=True, port=9000)
