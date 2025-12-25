import requests

url = "http://127.0.0.1:5000/predict"

data = {
    "age": 63,
    "sex": 1,
    "cp": 3,
    "trestbps": 145,
    "chol": ,
    "fbs": 1,
    "restceg": 0,
    "thalach": 150,
    "exang": 0,
    "oldpeak": 0.3,
    "slope": 0,
    "ca": 0,
    "thal": 1
}

response = requests.post(url, json=data)

print(response.text)
