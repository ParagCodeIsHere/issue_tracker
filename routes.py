# routes

from flask import render_template, request, redirect, url_for
from app import app, db
from models import Issue

@app.route('/')
def index():
    issues = Issue.query.all()
    return render_template('index.html', issues=issues)

@app.route('/add', methods=['POST'])
def add_issue():
    title = request.form['title']
    description = request.form['description']
    priority = request.form['priority']
    issue = Issue(title=title, description=description, priority=priority)
    db.session.add(issue)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/update/<int:id>', methods=['POST'])
def update_issue(id):
    issue = Issue.query.get(id)
    issue.status = request.form['status']
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete_issue(id):
    issue = Issue.query.get(id)
    db.session.delete(issue)
    db.session.commit()
    return redirect(url_for('index'))
