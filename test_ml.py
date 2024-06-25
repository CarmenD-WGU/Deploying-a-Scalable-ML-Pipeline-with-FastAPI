import pytest
import pandas as pd
import numpy as np
from ml.data import process_data
from ml.model import 

@pytest.fixture
def test_ml_data():
    return pd.read_csv("data/census.csv")

@pytest.fixture
def cat_features():
    return [
        "workclass",
        "education",
        "marital-status",
        "occupation",
        "relationship",
        "race",
        "sex",
        "native-country",
    ]


# DONE?: implement the first test. Change the function name and input as needed
def test_process_data(test_ml_data, cat_features):
    """
    # Test to ensure the process_data function returns expected results
    """
    encoder = None
    lb = None

    X_temp, y_temp, encoder, lb = process_data(
        test_ml_data,
        categorical_features = cat_features,
        label = "salary",
        training=True
    # do not need to pass encoder and lb as input
    )
    assert X_temp.shape[0] > 0, "X values array is empty"
    assert y_temp.shape[0] > 0, "y values array is empty"
    assert encoder is not None, "Did not produce trained OneHotEncoder"
    assert lb is not None, "Did not produce trained LabelBinarizer"


# TODO: implement the second test. Change the function name and input as needed
def test_two():
    """
    Test 
    """
    # Your code here
    pass


# TODO: implement the third test. Change the function name and input as needed
def test_three():
    """
    # add description for the third test
    """
    # Your code here
    pass
