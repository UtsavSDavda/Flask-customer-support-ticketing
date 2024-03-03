import pickle
from flask import Flask, render_template, request, redirect, url_for, session
import requests
import datetime
import boto3
table1 = ['user','user1']
app = Flask(__name__)

@app.route("/")
def intro():
    return render_template("myworld.html")
@app.route("/loguser", methods = ['GET'])
def login():
    return render_template("loguser.html")
#@app.route("/logout")
#def logout():

#@app.route("/employee")
#def employee():
    
@app.route("/user", methods=['POST'])
def user():
    name1 = request.form('username')
    pass1 = request.form('password')
    if name1 == table1[0] and pass1 == table1[1]:
        session['logged_in'] = True 
        session['Username'] = name1
        return render_template("user.html")
    else:
        return "Invalid username or password"







