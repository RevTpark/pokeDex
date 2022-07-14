from flask_restful import Resource
from flask import request
from models import Pokemon
from schema import TypeQueryScehma
from utils import algorithm, allowed_file, get_class, predict_pokemon
from werkzeug.utils import secure_filename
import os
import json

def build_result(poke):
    return {
        "id": poke.id,
        "dex_id": poke.dex_id,
        "name": poke.name,
        "image": poke.image,
        "primary_type": poke.primary_type,
        "description": poke.description,
        "secondary_type": poke.secondary_type,
        "is_mega": poke.is_mega,
    }


class GetPokemonDetailsAPI(Resource):

    def get(self, id):
        poke = Pokemon.query.get(id)
        if not poke:
            return {}, 404
        res = build_result(poke)
        return res, 200


class GetAllPokemonBasicAPI(Resource):

    def get(self):
        pokemon_list = Pokemon.query.all()
        res = []
        for poke in pokemon_list:
            res.append({
                "id": poke.id,
                "dex_id": poke.dex_id,
                "name": poke.name,
                "image": poke.image,
                "primary_type": poke.primary_type,
                "description": poke.description,
                "secondary_type": poke.secondary_type,
                "is_mega": poke.is_mega,
            })
        return res, 200


class SearchPokemonByName(Resource):

    def get(self, name):
        pokemon_list = Pokemon.query.filter(Pokemon.name.ilike(f"%{name}%")).all()
        res = []
        for poke in pokemon_list:
            res.append(build_result(poke))
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
                res.append(build_result(poke))
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
            res.append(build_result(poke))
        return res, 200


class PredictPokemonWithImage(Resource):

    def post(self):
        from app import app

        file = request.files['image']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            output = predict_pokemon(file_path)
            if os.path.exists(file_path):
                os.remove(file_path)
            poke = Pokemon.query.filter(Pokemon.name.ilike(f"%{output}%")).first()
            res = build_result(poke)
            return res, 200
            
        return {
            "error": "Wrong file type"
        }, 400


class GetTeamStrength(Resource):

    def post(self):
        data = json.loads(request.data)
        poke_data = {}
        for k, v in data.items():
            poke_data[k] = Pokemon.query.get(v)
        points = algorithm(poke_data)
        mssg = get_class(points)
        return { 
            "result": mssg[0],
            "class": mssg[1]
        }, 200
