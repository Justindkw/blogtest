from flask import Flask, request, redirect, url_for
from flask.templating import render_template
import sqlite3

app = Flask(__name__)



@app.route('/')
def home():
  db = sqlite3.connect('blog.db')
  cur = db.cursor()
  # cur.execute("DROP TABLE blog")
  # cur.execute("CREATE TABLE blog(id integer PRIMARY KEY, title text, subtitle text, author text, content text)")
  cur.execute("SELECT * FROM blog")
  return render_template('index.html', data = cur.fetchall())

@app.route('/post/<id>')
def post(id: int):
  db = sqlite3.connect('blog.db')
  cur = db.cursor()
  key = (id,)
  cur.execute("SELECT * FROM blog WHERE id=?", key)
  data = cur.fetchone()
  return render_template('post.html', title=data[1], subtitle=data[2], author=data[3], content=data[4])

@app.route('/add', methods=['POST','GET'])
def add():
  global topId
  if request.method == 'POST':
    db = sqlite3.connect('blog.db')
    cur = db.cursor()
    form = request.form
    cur.execute(f"INSERT INTO blog(title, subtitle, author, content) VALUES('{form['title']}', '{form['subtitle']}', '{form['author']}', '{form['content']}')")
    db.commit()
    return redirect(url_for('home'))
  return render_template('add.html')

@app.route('/about')
def about():
  return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)