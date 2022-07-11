from flask import url_for
from constants import class_names, ALLOWED_EXTENSIONS, mapping, pokemon_types
import numpy as np
import keras
import tensorflow as tf
import tensorflow_text 
import pathlib
import PIL

def load_model():
    model = keras.models.load_model("." + url_for('static', filename='models/pic_model'))
    return model

def load_text_model():
    model = keras.models.load_model("." + url_for('static', filename='models/text_model'), )
    return model

def predict_pokemon(filepath):
    model = load_model()
    img_height = 180
    img_width = 180
    new_pokemon_path = pathlib.Path(filepath)

    img = keras.utils.load_img(
        new_pokemon_path, target_size=(img_height, img_width)
    )
    img_array = keras.utils.img_to_array(img)
    img_array = np.expand_dims(img_array, 0) 

    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])
    guess = class_names[np.argmax(score)]
    return guess

def get_value(val):
  for k, v in mapping.items():
    if v == val:
      return k

def predict_text_pokemon(text):
    model = load_text_model()
    guess = get_value(np.argmax(model.predict(text)))
    return guess

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


def algorithm(data):
    from models import Types

    current_types = set()
    for k, v in data.items():
        current_types.add(v.primary_type)
        if v.secondary_type:
            current_types.add(v.secondary_type)
    
    attack_set = set()
    for ty in current_types:
        ty_details = Types.query.filter_by(name=ty).first()
        for ty2, val in ty_details.attack.items():
            if val == "2":
                attack_set.add(ty2)
    
    # extremely weak and weak set values as 2 and 1
    cant_defend = set()
    defense_set = set()
    for ty in current_types:
        ty_details = Types.query.filter_by(name=ty).first()
        for ty2, val in ty_details.defense.items():
            if val == "0.5" or val == "0":
                defense_set.add(ty2)
            elif val == "2":
                cant_defend.add(ty2)

    cant_defend = cant_defend.difference(attack_set).difference(defense_set)
    points = len(attack_set) + len(defense_set) - len(cant_defend)
    print(points)
