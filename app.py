from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def Wallbreaker():
  return render_template("wallbreaker.html")

if __name__ == "__main__":
  app.run()