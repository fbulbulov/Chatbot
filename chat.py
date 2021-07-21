import random
import json

import torch
from torch._C import int16

from model import NeuralNet
from nltk_utils import bag_of_words, tokenize

#checking device
device=torch.device('cuda' if torch.cuda.is_available() else 'cpu')

#opening the intents document
with open ("intents.json", 'r') as json_data:
    intents=json.load(json_data)

#uploading the trained weights 
FILE= "data.pth"
data=torch.load(FILE)

#torch model ingredients 
input_size=data['input_size']
hidden_size= data['hidden_size']
output_size=data['output_size']
all_words=data['all_words']
tags=data['tags']
model_state=data['model_state']

#importing the model
model=NeuralNet(input_size,hidden_size,output_size).to(devce)
model.load_state_dict(model_state)
model.eval()

#bot configuration 
name="Red Queen"
print ("Let's chat!(type quit to exit)")
while True:
    sentence=input ("You: ")
    if sentence = 'quit':
        break

#tokenization of the inputs
    sentence