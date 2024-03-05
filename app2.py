from flask import Flask

app=Flask(__name__)



@app.route('/')

def home():
    return '<h1>THIS IS HOME PAGE<h1>'



@app.route(('/about/<username>'))

def arya(username):
    return '<h1> hyy my name is %s ' %username




@app.route('/about/<int:ID>')

def hy(ID):
    return '<h1>my ID is %s ' %ID


app.run()


