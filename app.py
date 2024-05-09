from flask import Flask

app = Flask(__name__)


@app.route("/user")
def hello_admin():
    return "Hello User"


if __name__ == "__main__":
    app.run(debug=True)
