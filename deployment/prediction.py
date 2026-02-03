from utils import wrangle
import pickle
import path
import sys


dir = path.Path(__file__).abspath()
sys.path.append(dir.parent.parent)

# load model
path_to_model = './models/final_model.pkl'


with open(path_to_model, 'rb') as file:
    model = pickle.load(file)

def predict(data):
    """Make predictions"""
    processed = wrangle(data, test=True)
    result = model.predict(processed)
    output = ''
    if result == 0:
        output = "Not Likely To Have Bank Account"
    else:
        output = "Likely To Have a Bank Account"
    return output
