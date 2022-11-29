from flask import Flask, request
import numpy as np
import pickle

from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app, resorces={r'/*': {"orgins": '*'}})


@app.route("/")
def home():
    return "i think i want to clear this school now ky"


def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1, 5)
    loaded_model = pickle.load(open("./fruits.pickle", "rb"))
    print(type(loaded_model))
    result = loaded_model.predict(to_predict)
    return result[0]


@app.route("/model/api", methods=['POST', 'GET'])
def model_assignment():
    if request.method == "POST":
        contents = request.get_json()
        diameter = contents['diameter']
        weight = contents['weight']
        red = contents['red']
        blue = contents['blue']
        green = contents['green']
        fruits = []
        fruits.append(diameter)
        fruits.append(weight)
        fruits.append(red)
        fruits.append(green)
        fruits.append(blue)
        result = ValuePredictor(fruits)
        return result

    return "success"


app.run(debug=True)
