import os

from flask import Flask, render_template, redirect, session, request, session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from flask_session import Session
import sqlite3
from scrapers import *

from helpers import apology, login_required

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Creating a database connection
sqliteConnection = sqlite3.connect("denver_shows.sqlite", check_same_thread=False, isolation_level=None)
db = sqliteConnection.cursor()

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route('/login', methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username", [username]).fetchall()
        rows_length = len(rows)

        # Ensure username exists and password is correct
        if rows_length != 1 or not check_password_hash(rows[0][2], password):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0][0]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    """Register user"""
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        username = request.form.get("username")
        password_hash = generate_password_hash(request.form.get("password"))

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Ensure password was verified
        elif not request.form.get("password-verify"):
            return apology("must verify password", 403)

        elif request.form.get("password") != request.form.get("password-verify"):
            return apology("your password must match", 403)

        # Query database to check that username is unique
        rows = db.execute("SELECT COUNT(*) FROM users WHERE username = :username", [username])
        rows_length = rows.fetchone()
        print(rows_length)

        # Ensure username does not already exist
        if rows_length[0] > 0:
            return apology("that username already exists", 403)

        # Register the new user in the database
        db.execute("INSERT INTO users (username, hash) VALUES (:username, :password_hash)",
                   (username, password_hash))

        # Redirect user to login page
        return redirect("/login")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


@app.route('/')
@login_required
def homepage():
    return render_template("homepage.html")


@app.route('/red-rocks')
@login_required
def red_rocks():

    return render_template("redrocks.html")


@app.route('/ogden')
@login_required
def ogden():
    return render_template("ogden.html")


@app.route('/fillmore')
@login_required
def fillmore():
    return render_template("fillmore.html")


@app.route('/gothic')
@login_required
def gothic():
    return render_template("gothic.html")


@app.route('/mission')
@login_required
def mission():
    return render_template("mission.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.cli.command()
def scheduled_scrapers():
    """Run all scrapers."""
    print('Running scrapers')

    # Running the Red Rocks Amphitheater scraper
    red_rocks_scraper(db)

    # Running the Ogden Theatre scraper
    ogden_scraper(db)

    # Running the Mission Ballroom scraper
    mission_scraper(db)

    # Running the Fillmore Auditorium scraper
    fillmore_scraper(db)

    # Running the Gothic Theatre scraper
    gothic_scraper(db)

    print('Scrapers are complete!')


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)

# if __name__ == '__main__':
#     app.run()
