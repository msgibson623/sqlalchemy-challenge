from flask import Flask

app = Flask(_Climate App_)

@app.route('/')

def home():

    return "Precipitation"

@app.route('/')
def home():

    return "stations"

@app.route('/')
def home():

    return "tobs"