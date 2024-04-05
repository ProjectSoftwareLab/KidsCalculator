from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def hello():
    app.debug = True
    return render_template("index.html")

@app.route("/addition")
def addition():
    return render_template("addition.html")

@app.route("/substraction")
def substraction():
    return render_template("substraction.html")

@app.route("/multiplication")
def multiplication():
    return render_template("multiplication.html")

@app.route("/division")
def division():
    return render_template("division.html")

if __name__ == '__main__':
    app.run(debug=True)

