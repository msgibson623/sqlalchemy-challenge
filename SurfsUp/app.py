from flask import Flask, jsonify

import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
measurement = Base.classes.measurement
station = Base.classes.station
session = Session(engine)

app = Flask(__name__)

@app.route('/')

def home():

    return (
            f"Welcome to the Hawaii Climate Analysis API!<br/>"
            f"Available Routes:<br/>"
            f"/api/v1.0/precipitation<br/>"
            f"/api/v1.0/stations<br/>"
            f"/api/v1.0/tobs<br/>"
            f"/api/v1.0/temp/start<br/>"
            f"/api/v1.0/temp/start/end<br/>"
            f"<p>'start' and 'end' date should be in the format YYYYMMDD.</p>"

        )

@app.route('/api/v1.0/precipitation')
def date_prcp()
    f"prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
print("Query Date: ", prev_year)"

@app.route('/api/v1.0/stations')
def station_data()
    f"session.query(measurement.station, func.count(measurement.station)).group_by(measurement.station).order_by(func.count(measurement.station).desc()).all()"

@app.route('/api/v1.0/tobs')
def temp_observ()
    f"dtresult= session.query(measurement.tobs).filter(measurement.station=='USC00519281').filter(measurement.date>=prev_year).all()"

@app.route('/api/v1.0/temp/start')('/api/v1.0/temp/start/end')
def start_end()
    f"sel=[func.min(measurement.tobs),func.max(measurement.tobs),func.avg(measurement.tobs)]
result= session.query(* sel).filter(measurement.station=='USC00519281').all()
result"
    f""

if __name__ =="__main__":
    app.run()