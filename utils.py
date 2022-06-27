from flask import url_for
from constants import class_names, ALLOWED_EXTENSIONS, mapping
import numpy as np
import keras
import tensorflow as tf
import pathlib
import PIL

def load_model():
    model = keras.models.load_model("." + url_for('static', filename='models/pic_model'))
    return model

def load_text_model():
    model = keras.models.load_model("." + url_for('static', filename='models/text_model'), custom_objects={'CategoricalAccuracy': tf.keras.metrics.CategoricalAccuracy(name="accuracy")})
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