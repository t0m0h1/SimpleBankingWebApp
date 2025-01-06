# Simple banking web application

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Functions for bank operations 

balance = 0

def deposit(amount):
    balance += amount

def withdraw(amount):
    balance -= amount


def get_balance():
    return balance

def transfer(amount, recipient):
    balance -= amount
    recipient += amount


# Register and login functions
    
# def register(username, password):
#     # Check if username is already taken
#     return True
    
    

# def login(username, password):
#     # Check if username and password are correct
#     return True


@app.route('/') # Home page
def home():
    return render_template('index.html')
