from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
  return render_template("home.html")

@app.route("/about")
def about():
  return render_template("about.html")

@app.route("/<other>")
def catchall(other):
  return render_template("catchall.html", path = other)

if __name__ == "__main__":
  app.run(port=5000, debug=True)