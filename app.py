from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from decouple import config
from constants import pokemon_types

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = config("SQL_DATABASE_URI")
app.config["SECRET_KEY"] = config("SECRET_KEY")
db = SQLAlchemy(app)

from models import Pokemon

@app.route("/")
def home():
    data = Pokemon.query.filter(Pokemon.dex_id < 152).all()
    return render_template('home.html', data=data, types=pokemon_types)

@app.route("/types")
def type_classification():
    all_types = set()
    for i in range(len(pokemon_types)):
        for j in range(i+1, len(pokemon_types)):
            all_types.add((pokemon_types[i], pokemon_types[j]))
    used_types = set()
    for pokemon in Pokemon.query.all(): 
        if pokemon.secondary_type:
            used_types.add((pokemon.primary_type, pokemon.secondary_type)) 
            used_types.add((pokemon.secondary_type, pokemon.primary_type))
    unused = all_types.difference(used_types)
    return render_template('types.html', unused=unused)

from models import init_db_command, seed_pokemon_data
app.cli.add_command(init_db_command)
app.cli.add_command(seed_pokemon_data)

if __name__ == "__main__":
    app.run()
