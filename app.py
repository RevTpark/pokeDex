from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from decouple import config
from constants import pokemon_types, generations
import os
from utils import algorithm, allowed_file, get_class, predict_pokemon, predict_text_pokemon
from werkzeug.utils import secure_filename
from flask_restful import Api

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = config("DATABASE_URL")
app.config["SECRET_KEY"] = config("SECRET_KEY")
app.config['UPLOAD_FOLDER'] = 'uploads'
db = SQLAlchemy(app)

from models import Pokemon
from forms import AlgorithmForm

@app.route("/")
def home():
    data = Pokemon.query.filter(Pokemon.dex_id < 810).all()
    return render_template('home.html', data=data, types=pokemon_types, gens=generations)

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
    return render_template('types.html', unused=unused, types=pokemon_types)

@app.route("/guess-pokemon", methods=["GET", "POST"])
def guess_pokemon():
    if request.method == 'POST':
        file = request.files['file']
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            output = predict_pokemon(file_path)
            if os.path.exists(file_path):
                os.remove(file_path)
            pokemon = Pokemon.query.filter(Pokemon.name.ilike(f"%{output}%")).first()
            return render_template('guess_pokemon.html', pokemon=pokemon)

    return render_template("guess_pokemon.html")


# @app.route("/guess-text-pokemon", methods=["GET", "POST"])
# def guess_text_pokemon():
#     if request.method == "POST":
#         description = request.form['description']
#         output = predict_text_pokemon([description])
#         pokemon = Pokemon.query.filter(Pokemon.name.ilike(f"%{output}%")).first()
#         return render_template("guess_text_pokemon.html", pokemon=pokemon)
#     return render_template("guess_text_pokemon.html")


@app.route("/team-strength", methods=['GET', 'POST'])
def team_strength():
    form = AlgorithmForm()
    message = None
    if form.validate_on_submit():
        data = form.data
        data.pop("csrf_token")
        points = algorithm(data)
        message = get_class(points)
    return render_template('teams_strength.html', form=form, result=message)

from models import init_db_command, seed_pokemon_data
app.cli.add_command(init_db_command)
app.cli.add_command(seed_pokemon_data)

from api import GetPokemonDetailsAPI, GetAllPokemonBasicAPI, GetTeamStrength, SearchPokemonByName, SearchPokemonByType
api = Api(app, prefix="/api")
api.add_resource(GetPokemonDetailsAPI, "/pokemon/<int:id>")
api.add_resource(GetAllPokemonBasicAPI, "/pokemon/all")
api.add_resource(SearchPokemonByName, "/search/<string:name>")
api.add_resource(SearchPokemonByType, "/search")
# api.add_resource(PredictPokemonWithImage, "/predict")
api.add_resource(GetTeamStrength, "/team-strength")

