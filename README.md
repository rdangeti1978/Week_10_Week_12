# Week_10_Week_12

Breast Cancer Detection Web Application

# Dataset
Breast Cancer Wisconsin (Diagnostic) Data Set

# Attribute Information
1) id
2) diagnosis (M = malignant, B = benign)
---------------------
32) fractal_dimension_worst

Ten real-valued features are computed for each cell nucleus:
a) radius (mean of distances from center to points on the perimeter)
b) texture (standard deviation of gray-scale values)
c) perimeter
d) area
e) smoothness (local variation in radius lengths)
f) compactness (perimeter^2 / area - 1.0)
g) concavity (severity of concave portions of the contour)
h) concave points (number of concave portions of the contour)
i) symmetry
j) fractal dimension ("coastline approximation" - 1)

# Virtual Environment
Install the package for creating a virtual environment:
'$ sudo apt install python3-virtualenv'

Create a new virtual environment:
'python3 -m venv venv'
or
'$ virtualenv venv'

Activate virtual environment:
'$ source venv/bin/activate'

# Python Packages
Inside virtual environment install the dependencies written in requirements.txt:
'$ pip3 install -r requirements.txt'

# Train
Run the script in code_model_training/train.py, this script takes the input data and outputs a trained model and a pipeline for web service:
'$ python3 code_model_training/train.py'

# Web Application
Test web application by running:
'$ flask run -p 5000'

Test web application related info/health/predict of model on ubuntu terminal:
Please refer syntax from tests/example_calls.txt file  

Test web application on browser by running:
'http://127.0.0.1:5000/' 

1. Machine Learning (ML) Predictive Model Information And Version:
'http://127.0.0.1:5000/info1'

2. Machine Learning (ML) Predictive Model Health Service:
'http://127.0.0.1:5000/health1'

3. Machine Learning (ML) Predictive Model For Manual Dataset:
'http://127.0.0.1:5000/manual

4. Machine Learning (ML) Predictive Model For Sample Dataset:
'http://127.0.0.1:5000/sample

# Docker
Dockerfile to create an image for web application inside a container:
'$ docker build -t dcfkwbap .'

Test application using docker:
'$ docker run -p 5000:5000 dcfkwbap'
