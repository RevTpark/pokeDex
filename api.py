from flask_restful import Resource
from flask import request
from models import Pokemon
from schema import TypeQueryScehma

class GetPokemonDetailsAPI(Resource):

    def get(self, name):
        poke = Pokemon.query.filter(Pokemon.name.ilike(f"%{name}%")).first()
        if not poke:
            return {}, 404
        res = {
            "dex_id": poke.dex_id,
            "name": poke.name,
            "image": poke.image,
            "primary_type": poke.primary_type,
            "secondary_type": poke.secondary_type,
            "is_mega": poke.is_mega,
        }
        return res, 200


class GetAllPokemonBasicAPI(Resource):

    def get(self):
        pokemon_list = Pokemon.query.all()
        res = []
        for poke in pokemon_list:
            res.append({
                "dex_id": poke.dex_id,
                "name": poke.name,
                "image": poke.image,
                "primary_type": poke.primary_type,
                "secondary_type": poke.secondary_type,
                "is_mega": poke.is_mega,
            })
        return res, 200


class SearchPokemonByName(Resource):

    def get(self, name):
        pokemon_list = Pokemon.query.filter(Pokemon.name.ilike(f"%{name}%")).all()
        res = []
        for poke in pokemon_list:
            res.append({
                "dex_id": poke.dex_id,
                "name": poke.name,
                "image": poke.image,
                "primary_type": poke.primary_type,
                "secondary_type": poke.secondary_type,
                "is_mega": poke.is_mega,
            })
        return res, 200


class SearchPokemonByType(Resource):
    schema = TypeQueryScehma()

    def get(self):
        errors = self.schema.validate(request.args)
        if errors:
            return errors, 400
        
        type1 = request.args['type1']
        type2 = request.args.get('type2', None)

        if not type2:
            pokemon_list = Pokemon.query.filter((Pokemon.primary_type == type1) | (Pokemon.secondary_type == type1)).all()
            res = []
            for poke in pokemon_list:
                res.append({
                    "dex_id": poke.dex_id,
                    "name": poke.name,
                    "image": poke.image,
                    "primary_type": poke.primary_type,
                    "secondary_type": poke.secondary_type,
                    "is_mega": poke.is_mega,
                })
            return res, 200

        pokemon_list = Pokemon.query.filter(
            (
                (Pokemon.primary_type == type1) & 
                (Pokemon.secondary_type == type2)
            ) | 
            (
                (Pokemon.primary_type == type2) & 
                (Pokemon.secondary_type == type1)
            )
        )
        res = []
        for poke in pokemon_list:
            res.append({
                "dex_id": poke.dex_id,
                "name": poke.name,
                "image": poke.image,
                "primary_type": poke.primary_type,
                "secondary_type": poke.secondary_type,
                "is_mega": poke.is_mega,
            })
        return res, 200

