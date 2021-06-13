from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/hey/<name>")
def hey(name):
    return "<p>hey {} </p>".format(name)

@app.route("/months_eng/<month>")
def get_month(month):
    month = int(month)
    months = ['Jan', 'Feb', 'Mar']
    return "{}".format(months[month-1])


@app.route("/wow")
def wow():
    what = request.args.get('what', 'default')
    return what

@app.route('/postit', methods=['POST', 'GET'])
def postit():
    if request.method == 'POST':
        message = 'hello {}'.format(request.form['name'])
        return render_template('hello.html', message=message)
        # return 'hello {}'.format(request.form['name'])
    return """
        <form action="" method="post">
        <p>
            <label for="name">Your name</label>
            <input type="text" name="name">
        </p>
        <p>
            <input type="submit">
        </p>
    </form>
    """
    