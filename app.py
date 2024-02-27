import pickle
from flask import Flask, render_template, request, redirect, url_for, session
import requests
import numpy as np
import pandas as pd
import matplotlib
import datetime
import boto3
app = Flask(__name__)

@app.route("/")
def intro():
    return "HI BRO"
@app.route("/Hibro")
@app.route("/Hibro/<name>")
def name(name=None):
    return render_template("hi1.html",name=name)






