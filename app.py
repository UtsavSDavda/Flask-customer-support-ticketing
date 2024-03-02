import pickle
from flask import Flask, render_template, request, redirect, url_for, session
import requests
import datetime
import boto3
app = Flask(__name__)

@app.route("/")
def intro():
    return render_template("myworld.html")
@app.route("/loguser", methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("myworld.html")
    elif request.method == 'POST':
        name1 = request.form('username')
        pass1 = request.form('password')
        response = table.get_item(Key={'username': username})
        if 'Item' not in response:
            return "Invalid username or password"
        hashed_password = response['Item']['password']
        if bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
            return render_template("user.html")
        else:
            return "Invalid username or password"

#@app.route("/logout")
#def logout():

#@app.route("/main")
#def main():

#@app.route("/employee")
#def employee():

#@app.route("/user")
#def user():







