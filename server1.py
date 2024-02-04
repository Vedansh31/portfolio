from flask import Flask, render_template

app = Flask(__name__)

# Connection to HomePage
@app.route("/")
def my_home():
    return render_template('index.html')