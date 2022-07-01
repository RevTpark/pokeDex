from flask_wtf import FlaskForm
from wtforms_sqlalchemy.fields import QuerySelectField
from models import Pokemon

def get_pokemon():
    return Pokemon.query.filter(Pokemon.dex_id < 152, Pokemon.image != "")

class AlgorithmForm(FlaskForm):
    for i in range(1, 7):
        locals()[f'poke{i}'] = QuerySelectField(label=f"Pokemon {i}", query_factory=get_pokemon, get_label=lambda x: x.name, get_pk=lambda x: x.id)
