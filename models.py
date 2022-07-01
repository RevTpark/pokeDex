import numpy
from app import db
import click
from flask.cli import with_appcontext
import pandas as pd


class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    dex_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=True)
    image = db.Column(db.String, nullable=True, server_default='')
    primary_type = db.Column(db.String, nullable=False)
    secondary_type = db.Column(db.String, nullable=True)
    is_mega = db.Column(db.Boolean, nullable=False, default=False)

class Types(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String, nullable=False)
    attack = db.Column(db.JSON, nullable=False)
    defense = db.Column(db.JSON, nullable=True)

@click.command('init-db')
@with_appcontext
def init_db_command():
    db.create_all()   
    click.echo('Initialized the database.')


@click.command('seed-data')
@with_appcontext
def seed_pokemon_data():
    df = pd.read_csv("pokebase.csv")
    for idx, row in df.iterrows():
        poke = Pokemon(
            dex_id=row['dex_id'],
            name=row['name'],
            primary_type=row['primary_type'],
            secondary_type= None if type(row['secondary_type']) == float else row['secondary_type'],
            image="" if type(row['image']) == float else row['image'],
            is_mega=row['is_mega'],
            description=None if type(row['Description']) == float else row['Description'] 
        )
        db.session.add(poke)
        db.session.commit()
    
    df = pd.read_csv('typebase.csv')
    for idx, row in df.iterrows():
        new_type = Types(
            name=row['name'],
            attack=row['attack'],
            defense=row['defense']
        )
        db.session.add(new_type)
        db.session.commit()
    
    click.echo('Seeded the pokebase.')