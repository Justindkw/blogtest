from flask import Flask, request, redirect, url_for
from flask_basicauth import BasicAuth
from flask.templating import render_template
import sqlite3
from sqlAlchemy import *


db.create_all()
db.init_app(app) 

app.config['BASIC_AUTH_USERNAME'] = 'justin'
app.config['BASIC_AUTH_PASSWORD'] = 'ember'

basic_auth = BasicAuth(app)

@app.route('/')
def home():
  print(Blog.query.all()[0])
  return render_template('index.html', data = Blog.query.all())

@app.route('/post/<id>')
def post(id: int):
  return render_template('post.html', post = Blog.query.filter_by(id = id).first())

@app.route('/add', methods=['POST','GET'])
@basic_auth.required
def add():
  if request.method == 'POST':
    form = request.form
    db.session.add(Blog(title = form['title'], subtitle = form['subtitle'], author = form['author'], content = form['content']))
    db.session.commit()
    return redirect(url_for('home'))
  return render_template('add.html')

@app.route('/about')
def about():
  return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)