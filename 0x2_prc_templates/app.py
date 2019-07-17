from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/hello')
def hello_template():
    word = "Template!"
    return render_template('hello_template.html', word = word)


if __name__ == '__main__':
    app.run()
