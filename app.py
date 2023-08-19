from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index2.html")


@app.route("/contacts")
def contacts():
    return render_template("contacts.html")


@app.route("/languages")
def languages():
    return render_template("languages.html")


@app.route("/projects")
def projects():
    return render_template("projects.html")


if __name__ == "__main__":
    app.run()
