import pytest
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from ml.data import process_data
from ml.model import compute_model_metrics, train_model

@pytest.fixture
def raw_data():
    return pd.read_csv("data/census.csv")

@pytest.fixture
def pytest_data():
    df = pd.read_csv("data/census.csv")
    df.sample(500) #to reduce processing requirements
    return train_test_split(df)
    

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


# DONE?: implement the third test. Change the function name and input as needed
def test_data_existance():
    """
    Check that the sahpe of the dataframe loaded has rows and the expected number of columns

    INPUT:
    raw_data - a dataframe containing the data from census.csv

    RETURNS:
    nothing
    """
    
    assert raw_data.shape[0] > 0, "Dataframe contains no rows"
    assert raw_data.shape[1] == 15, "Dataframe has incorrect number of columns"



# DONE?: implement the first test. Change the function name and input as needed
def test_process_data(pytest_data, cat_features):
    """
    Test to ensure the process_data function returns expected results
    using a sample of the dataset

    INPUTS:
    pytest_data - a sample of the original data from the CSV 
                    split into training and test datasets
    cat_fatures -  a list of the categorical features in the dataset

    RETURNS: 
    nothing

    """
    encoder = None
    lb = None

    train, test = pytest_data

    X_temp, y_temp, encoder, lb = process_data(
        train,
        categorical_features = cat_features,
        label = "salary",
        training=True
    # do not need to pass encoder and lb as input
    )
    assert X_temp.shape[0] > 0, "X values array is empty"
    assert y_temp.shape[0] > 0, "y values array is empty"
    assert encoder is not None, "Did not produce trained OneHotEncoder"
    assert lb is not None, "Did not produce trained LabelBinarizer"


# DONE?: implement the second test. Change the function name and input as needed
def test_compute_model_metrics(pytest_data, cat_features):
    """
    Test the compute_model_metrics function to ensure the scores produced are 
    within the possible range for valid scores using a sample of the dataset

    INPUTS:
    pytest_data - a sample of the original data from the CSV 
                    split into training and test datasets
    cat_fatures -  a list of the categorical features in the dataset

    RETURNS: 
    nothing
    """
    encoder = None
    lb = None
    train, test = pytest_data

    X_temp, y_temp, encoder, lb = process_data(
        train,
        categorical_features = cat_features,
        label = "salary",
        training=True
    # do not need to pass encoder and lb as input
    )

    X_test, y_test, _, _ = process_data(
    test,
    categorical_features=cat_features,
    label="salary",
    training=False,
    encoder=encoder,
    lb=lb,  
    )

    preds = train_model(X_temp, y_temp).predict(X_test)

    prec, recall, f_beta = compute_model_metrics(y_test, preds)

    # Your code here
    assert 0 <= f_beta <= 1, "Invalid f_beta score: outside 0-1 bounds"
    assert 0 <= prec  <= 1, "Invalid precision score: outside 0-1 bounds"
    assert 0 <= recall  <= 1, "Invalid recall score: outside 0-1 bounds"


