# coding=utf-8
from flask import Flask, redirect, render_template

from website.constants import DISCORD_INVITE, LOCATIONS

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", locations=LOCATIONS)


@app.route("/wow")
def wow():
    return render_template("wow.html", locations=LOCATIONS)


@app.route("/invite")
def invite():
    return redirect(DISCORD_INVITE)


if __name__ == "__main__":
    app.run()
