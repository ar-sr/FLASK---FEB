from flask import Flask

comp=Flask(__name__)



@comp.route('/')

def home():
    return '<h1>THIS IS HOME PAGE<h1>'



@comp.route('/about/<arya>')

def arya(username):
    return '<h1> hyy my name is %s ' %username

comp.run()
