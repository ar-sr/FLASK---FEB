from flask import Flask

app=Flask(__name__)



@app.route('/')

def home():
    return '<h1>ARYA SR<h1>'



@app.route(('/about'))

def about():
    return '<h1>ABOUT ME<h1>'



@app.route(('/qualification'))

def qualification():
    return '<h1>MY QUA<h1>'


@app.route(('/marks'))

def marks():
    return '<h1>MY MARKS<h1>'




app.run()


