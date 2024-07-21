#Author rdangeti

# Local imports
import datetime
import json

# third party lib imports
from flask import Flask, request, render_template
import pandas as pd
import joblib
import numpy as np

from ms import app
from ms.functions import get_model_response, get_model_response1


model_name = "Breast Cancer Wisconsin (Diagnostic) Application"
model_file = 'model_binary.dat.gz'
version = "v1.0.0"

app = Flask(__name__)
model = joblib.load('model/model_binary.dat.gz')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/info', methods=['GET'])
def info():
    """Return model information, version, how to call"""
    result = {}
    result["name"] = model_name 
    result["version"] = version
    
    return result


@app.route('/health', methods=['GET'])
def health():
    """Return service health"""
    serves = {}
    serves["health"] = 'ok'
    
    return serves


@app.route('/predict', methods=['POST'])
def predict():

    feature_dict = request.get_json()

    if not feature_dict:
         return {
              'error' : 'Body is empty.'
            }, 500

    try:
        response = get_model_response(feature_dict)
    except ValueError as e:
        return {'error': str(e).split('\n')[-1].strip()}, 500

    return response, 200

@app.route('/info1', methods=['GET'])
def info1():
    
    return render_template('index.html', information = 'Breast Cancer Wisconsin (Diagnostic) Application v1.0.0')


@app.route('/health1', methods=['GET'])
def health1():

    return render_template('index.html', service = 'Ok')


@app.route('/manual', methods=['GET', 'POST'])
def manual():

    return render_template('manual.html')


@app.route('/diagnostic', methods=['GET', 'POST'])
def diagnostic():
    if request.method == "POST":
           radmn = request.form.get("radius_mean")
           texmn = request.form.get("texture_mean")
           perimn = request.form.get("perimeter_mean")
           armn = request.form.get("area_mean")
           smthmn = request.form.get("smoothness_mean")
           compmn = request.form.get("compactness_mean")
           concmn = request.form.get("concavity_mean")
           conpotmn = request.form.get("concave points_mean")
           symmn = request.form.get("symmetry_mean")
           fradimn = request.form.get("fractal_dimension_mean")
           radse = request.form.get("radius_se")
           texse = request.form.get("texture_se")
           perise = request.form.get("perimeter_se")
           arse = request.form.get("area_se")
           smthse = request.form.get("smoothness_se")
           compse = request.form.get("compactness_se")
           conse = request.form.get("concavity_se")
           conpotse = request.form.get("concave points_se")
           symse = request.form.get("symmetry_se")
           fradise = request.form.get("fractal_dimension_se")
           radwt = request.form.get("radius_worst")
           texwt = request.form.get("texture_worst")
           periwt = request.form.get("perimeter_worst")
           arwt = request.form.get("area_worst")
           smthwt = request.form.get("smoothness_worst")
           compwt = request.form.get("compactness_worst")
           concwt = request.form.get("concavity_worst")
           conpotwt = request.form.get("concave points_worst")
           syswt = request.form.get("symmetry_worst")
           fradiwt= request.form.get("fractal_dimension_worst")
           X = pd.DataFrame([[radmn, texmn, perimn, armn, smthmn, compmn, 
                concmn, conpotmn, symmn, fradimn, radse, texse, perise, arse, 
                smthse, compse, conse, conpotse, symse, fradise, radwt, texwt, 
                periwt, arwt, smthwt, compwt, concwt, conpotwt, syswt, fradiwt]], 
                columns = ["radius_mean", "texture_mean", "perimeter_mean", 
                           "area_mean", "smoothness_mean", "compactness_mean", 
                           "concavity_mean", "concave points_mean", "symmetry_mean", 
                           "fractal_dimension_mean", "radius_se", "texture_se", 
                           "perimeter_se", "area_se", "smoothness_se", "compactness_se", 
                           "concavity_se", "concave points_se", "symmetry_se", 
                           "fractal_dimension_se", "radius_worst", "texture_worst", 
                           "perimeter_worst", "area_worst", "smoothness_worst", 
                           "compactness_worst", "concavity_worst", "concave points_worst", 
                           "symmetry_worst", "fractal_dimension_worst"])
           prediction = model.predict(X)[0]
           print(prediction)
           if prediction == 1:
                res_val = "breast cancer"
           else:
                res_val = "no breast cancer"
           
    else:
           print("Please enter valid data")

    return render_template('manual.html', output = 'Patient has {}'.format(res_val))


@app.route('/sample', methods=['GET', 'POST'])
def sample():

    return render_template('sample.html')


@app.route('/jsnpredict', methods=['GET'])
def jsnpredict():

    jsdata = "application/test_data.json"

    try:
        with open(jsdata, "r") as p:
            print(json.load(p))
    except json.decoder.JSONDecodeError:
            print("Error in file/json")
    
    try:
        with open(jsdata, "r") as p:
            response1 = get_model_response1(json.load(p))
    except ValueError as e:
            return {'error': str(e).split('\n')[-1].strip()}, 500

    return render_template('sample.html', result1 = '{}'.format(response1))


@app.route('/jsnpredict1', methods=['GET'])
def jsnpredict1():

    jsdata1 = "application/test_data1.json"

    try:
        with open(jsdata1, "r") as p1:
            print(json.load(p1))
    except json.decoder.JSONDecodeError:
            print("Error in file/json")
    
    try:
        with open(jsdata1, "r") as p1:
            response2 = get_model_response1(json.load(p1))
    except ValueError as e:
            return {'error': str(e).split('\n')[-1].strip()}, 500

    return render_template('sample.html', result2 = '{}'.format(response2))

 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
