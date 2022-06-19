from app import db
import click
from flask.cli import with_appcontext
import requests
from bs4 import BeautifulSoup


class Pokemon(db.Model):

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    dex_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String, nullable=False)
    image = db.Column(db.String, nullable=True, server_default='')
    primary_type = db.Column(db.String, nullable=False)
    secondary_type = db.Column(db.String, nullable=True)
    is_mega = db.Column(db.Boolean, nullable=False, default=False)


@click.command('init-db')
@with_appcontext
def init_db_command():
    db.create_all()   
    click.echo('Initialized the database.')


@click.command('seed-data')
@with_appcontext
def seed_pokemon_data():
    url = "https://pokemondb.net/pokedex/all"
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36"}
    r = requests.get(url, headers=headers)

    soup = BeautifulSoup(r.content, "html.parser")
    pokemon_list = soup.find("table", {"id": "pokedex"}).find_all('tr')

    for pokemon in pokemon_list[1:]:
        poke_id = int(pokemon.find('span', {"class": "infocard-cell-data"}).text)
        name = pokemon.find('a', {"class": "ent-name"}).text
        poke_types = pokemon.find_all('a', {"class": "type-icon"})
        primary_type = poke_types[0].text
        secondary_type = None
        if len(poke_types) != 1:
            secondary_type = poke_types[1].text
        
        is_mega = False
        if pokemon.find('small', {"class": "text-muted"}):
            name = pokemon.find('small', {"class": "text-muted"}).text
            is_mega = True

        image = ""
        
        new_pokemon = Pokemon(
            dex_id=poke_id, 
            name=name, 
            primary_type=primary_type, 
            secondary_type=secondary_type, 
            image=image,
            is_mega=is_mega
        )
        db.session.add(new_pokemon)
        db.session.commit()
    click.echo('Seeded the pokebase.')