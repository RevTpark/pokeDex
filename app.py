from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from decouple import config
import os


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = config("SQL_DATABASE_URI")
app.config["SECRET_KEY"] = config("SECRET_KEY")
db = SQLAlchemy(app)

from models import Pokemon
from constants import poke_data
import re

@app.route("/")
def home():
    data = Pokemon.query.filter(Pokemon.dex_id < 152).all()
    return render_template('home.html', data=data)

from models import init_db_command, seed_pokemon_data
app.cli.add_command(init_db_command)
app.cli.add_command(seed_pokemon_data)

if __name__ == "__main__":
    app.run()
