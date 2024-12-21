from flask import Flask, render_template, flash, request
import os

app = Flask(__name__)

app.secret_key = os.getenv("SECRET_KEY")
app.config["DEBUG"] = False

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/generalizedCouponCollector', methods=['POST', 'GET'])
def greet():
    return render_template("generalizedCouponCollector.html")




