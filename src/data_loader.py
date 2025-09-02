from sklearn.datasets import load_iris
from logger import logging

def load_data():
    logging.info("Loading Iris dataset...")
    data = load_iris(as_frame=True)
    X = data.data
    y = data.target
    logging.info(f"Dataset loaded successfully with {X.shape[0]} samples and {X.shape[1]} features.")
    return X, y
