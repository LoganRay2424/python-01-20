from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello world!"

@app.route("/abc")
def new_page():
    return render_template("index.html")

@app.route("/guest/<name>")
def new_guest(name):
    cube1 = random.randint(1,6)
    cube2 = random.randint(1,6)
    return render_template("guest.html", guest_from_url = name, cube1= cube1, cube2 = cube2)


if __name__=="__main__":
    app.run(debug=True)