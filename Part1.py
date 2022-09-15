#Imports
import sys
from api_comm import *
from Voice_recorder import *


audio()

#variables
filename = track_name


audio_url = Upload(filename)
save_transcipt(audio_url,filename)

print('done')

from Sentence__analysis import predict

predict()