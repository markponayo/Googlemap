from flask import Flask, render_template

app = Flask(__name__)

API_KEY = "AIzaSyB9SK7P_PfsWBaKV2yH8UjVe5FmFiArcEI"

@app.route("/")
def index():
    return render_template("template.html", api_key=API_KEY)

if __name__ == "__main__":
    app.run(debug=True)
