from tempfile import mkdtemp

from flask import Flask, render_template, redirect, session, request, session
from pip._vendor.requests import Session
import sqlite3
import os

# Configure application

app = Flask(__name__)

# Creating a database connection
sqliteConnection = sqlite3.Connection("denver_shows.db")

# Configure session to use filesystem (instead of signed cookies)
# app.config["SESSION_FILE_DIR"] = mkdtemp()
# app.config["SESSION_PERMANENT"] = False
# app.config["SESSION_TYPE"] = "filesystem"
# Session(app)

@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/register')
def register():
    return render_template("register.html")


@app.route('/')
def homepage():
    return render_template("homepage.html")


@app.route('/red-rocks')
def red_rocks():
    return render_template("redrocks.html")


@app.route('/ogden')
def ogden():
    return render_template("ogden.html")


@app.route('/fillmore')
def fillmore():
    return render_template("fillmore.html")


@app.route('/gothic')
def gothic():
    return render_template("gothic.html")


@app.route('/mission')
def mission():
    return render_template("mission.html")


if __name__ == '__main__':
    app.run()
