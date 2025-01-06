# Simple banking web application

from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Required for flash messages

# Mock database
users = {}  # Format: {username: {"password": "hashed_password", "balance": 0}}

def deposit(username, amount):
    users[username]["balance"] += amount

def withdraw(username, amount):
    if users[username]["balance"] >= amount:
        users[username]["balance"] -= amount
        return True
    return False

def get_balance(username):
    return users[username]["balance"]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username in users:
            flash("Username already exists!")
        else:
            users[username] = {"password": password, "balance": 0}
            flash("Registration successful!")
            return redirect(url_for("home"))
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username in users and users[username]["password"] == password:
            flash("Login successful!")
            return redirect(url_for("dashboard", username=username))
        else:
            flash("Invalid username or password!")
    return render_template("login.html")

@app.route("/dashboard/<username>")
def dashboard(username):
    if username in users:
        balance = get_balance(username)
        return render_template("dashboard.html", username=username, balance=balance)
    flash("User not found!")
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
