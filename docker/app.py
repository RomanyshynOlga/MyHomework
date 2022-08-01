from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, Olga'

@app.route('/hello')
def answer():
    return 'Hi!'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)