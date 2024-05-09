from flask import Flask

app = Flask(__name__)


@app.route("/mother")
def hello_admin():
    return "Hello User"


if __name__ == "__main__":
    app.run(debug=True)
