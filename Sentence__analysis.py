from opcode import opname
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
import pandas as pd
from Voice_recorder import *
import tensorflow_hub as hub
from sklearn.preprocessing import OneHotEncoder

model = load_model('emotion_model.h5')

with open('Track.wav.txt','r') as f:
    lines = f.readlines()
f.close()

U_S_E = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4"
)

#In the U_S_E variable the link can be replaced with the universal senntence encoder file pth if its stored your local machine

state_ment = np.array(list(lines))

class_names = ['anger','fear','joy','love','sadness','surprise']
text = U_S_E(state_ment)


def predict():
    emotion = model.predict(text)
    prediction = class_names[np.argmax(emotion)]
    print(prediction)

