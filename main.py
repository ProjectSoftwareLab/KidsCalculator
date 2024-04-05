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

if __name__ == '__main__':
    app.run(debug=True)

