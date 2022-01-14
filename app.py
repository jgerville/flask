from flask import Flask, render_template, abort

app = Flask(__name__)

route_bullets = [
  {"id": 1, "text": "Unlike with MVC frameworks, in Flask views refer to routes"},
  {"id": 2, "text": "You can use more than 1 route decorator with a view"},
  {"id": 3, "text": "So far, setting up routes is very simple, and similar to Express"},
]

jinja_bullets = [
  {"id": 4, "text": "To get a static asset URL, much like Rails, we use: {% raw %}url_for('static', filename = 'xyz.abc'){% endraw %}"},
  {"id": 5, "text": "Unlike with ERB, we need something special to end for loops: {% raw %}{% endfor %}{% endraw %}"},
  {"id": 6, "text": "To end if blocks, we need {% raw %}{% endif %}{% endraw %}"},
]

@app.route("/")
@app.route("/home")
def home():
  return render_template("home.html")

@app.route("/about")
def about():
  return render_template("about.html", route_bullets = route_bullets, jinja_bullets = jinja_bullets)

@app.route("/bullets/<int:num>")
def bullet(num):
  resp = next((item["text"] for item in route_bullets if item["id"] == num ), None)
  if resp is None:
    resp = next((item["text"] for item in jinja_bullets if item["id"] == num ), None)
    if resp is None:
      abort(404, description="Sorry, this bullet point doesn't exist.")
  return resp

@app.route("/<other>")
def catchall(other):
  return render_template("catchall.html", path = other)

if __name__ == "__main__":
  app.run(port=5000, debug=True)