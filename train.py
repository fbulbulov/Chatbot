import numpy as np
import random 
import json 
import torch
import torch.nn as nn
import nltk
from torch.utils.data import Dataset,DataLoader
#from nltk_utils import bag_of_words, tokenize, stem
from model import NeuralNet #importing the model from model.py

with open('intents.json', 'r') as f: #loading our json intents files
    intents=json.load(f)

