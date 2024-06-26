import json
import requests

# DONE: send a GET using the URL http://127.0.0.1:8000
local_URL = "http://127.0.0.1:8000/"
r = requests.get(local_URL)

# DONE: print the status code
print("Get request status code: ", r.status_code)
# DONE?: print the welcome message
print("Welcome Message:", r.json())



data = {
    "age": 37,
    "workclass": "Private",
    "fnlgt": 178356,
    "education": "HS-grad",
    "education-num": 10,
    "marital-status": "Married-civ-spouse",
    "occupation": "Prof-specialty",
    "relationship": "Husband",
    "race": "White",
    "sex": "Male",
    "capital-gain": 0,
    "capital-loss": 0,
    "hours-per-week": 40,
    "native-country": "United-States",
}

test_data = {
    37,
    "Private",
    178356,
    "HS-grad",
    10,
    "Married-civ-spouse",
    "Prof-specialty",
    "Husband",
    "White",
    "Male",
    0,
    0,
    40,
    "United-States",
}

# DONE?: send a POST using the data above
r = requests.post(local_URL+"data?",
                         data = data)


# DONE: print the status code
print("Post request status code: ", r.status_code)
# DONE: print the result
print("Inferance result: ", r.json())
