from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h1>Hello world!</h1>"


@app.route("/sobre")
def sobre():
    return "<h2>Página Sobre</h2>"


if __name__ == "__main__":
    app.run(debug=True)
