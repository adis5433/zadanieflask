
from flask import Flask, render_template, redirect, request

app = Flask(__name__)


@app.route("/mypage/me", methods=["GET"])
def aboutme():
    return render_template("omnie.html")


@app.route("/mypage/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        msg = request.form["txt"]
        return  msg
    else:
        return render_template("Kontakt.html")
