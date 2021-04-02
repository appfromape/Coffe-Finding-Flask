from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, MetaData, Table, Column, ForeignKey, Integer
from sqlalchemy.ext.automap import automap_base
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = "any-string-you-want-just-keep-it-secret"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

engine = create_engine("sqlite:///cafes.db")
metadata = MetaData()
metadata.reflect(engine, only=['cafe'])
Base = automap_base(metadata=metadata)
Base.prepare()
Cafe = Base.classes.cafe

@app.route('/')
def index():
    coffes = db.session.query(Cafe).all()
    return render_template("index.html", all_coffes=coffes)

if __name__ == "__main__":
    app.run(debug=True)