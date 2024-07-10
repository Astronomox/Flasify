from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
  return("I tried to render a template on RENDER but it says Exits on Status 1")


if __name__ == "__main__":
  app.run(debug=True)