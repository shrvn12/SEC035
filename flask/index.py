from flask import Flask, render_template_string, request, redirect, url_for, session, flash
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

from flask import request
@app.route('/form')
def form():
    return '''
        <form action="/result" method="get">
            Name: <input name="name">
            <input type="submit">
        </form>
    '''

@app.route('/result')
def result():
    name = request.args.get('name')
    return f"Hello, {name}!"

@app.route('/admin')
def admin():
    name = request.args.get('name')
    return redirect(url_for('user', name=name or "admin"))

@app.route('/user/<name>')
def user(name):
    return f"Welcome, {name}"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        return f"Welcome, {user}!"
    return '''
        <form method="post">
            Username: <input name="username">
            <input type="submit">
        </form>
    '''

app.secret_key = 'secret123'

@app.route('/set/<name>')
def set_session(name):
    session['user'] = name
    return 'Session set!'

@app.route('/get')
def get_session():
    return f"User: {session.get('user')}"

import os
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
        return 'File uploaded!'
    return '''
        <form method="post" enctype="multipart/form-data">
            <input type="file" name="file">
            <input type="submit">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
