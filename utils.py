from flask import url_for
from constants import class_names, ALLOWED_EXTENSIONS, mapping, points_mapping 
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
    # Values {0.0, 0.25, 0.5, 1.0, 2.0, 4.0}
    # Points {4, 2, 1, 0, -2, -4}
    defense_set = {
        0.0: set(),
        0.25: set(),
        0.5: set(),
        1.0: set(),
        2.0: set(),
        4.0: set()
    }
    for _, v in data.items():
        if v.secondary_type:
            ty1_details = Types.query.filter_by(name=v.primary_type).first()
            ty2_details = Types.query.filter_by(name=v.secondary_type).first()
            for def1, def2 in zip(ty1_details.defense.items(), ty2_details.defense.items()):
                name, total_val = def1[0], float(def1[1]) * float(def2[1])
                defense_set[total_val].add(name)
        else:
            ty1_details = Types.query.filter_by(name=v.primary_type).first()
            for ty_name, val in ty1_details.defense.items():
                defense_set[float(val)].add(ty_name)
    
    points = len(attack_set)*points_mapping['attack'] + len(defense_set[0.0])*points_mapping['immune'] + len(defense_set[0.25])*points_mapping['resistant'] \
            + len(defense_set[0.5])*points_mapping['defendable'] + len(defense_set[2.0])*points_mapping['weak'] + len(defense_set[4.0])*points_mapping['extremely_weak'] \
            + len(defense_set[2.0].intersection(attack_set))*points_mapping['weak_defense'] + len(defense_set[4.0].intersection(attack_set))*points_mapping['extremely_weak_defense']
    print(points)
