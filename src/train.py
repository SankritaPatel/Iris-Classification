from sklearn.model_selection import train_test_split
from joblib import dump
from logger import logging

def train(X, y, model, config):
    logging.info("Splitting data into train and test sets...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=config["train"]["test_size"],
        random_state=config["train"]["random_state"]
    )
    logging.info(f"Training data shape: {X_train.shape}, Test data shape: {X_test.shape}")
    
    logging.info("Starting model training...")
    model.fit(X_train, y_train)
    logging.info("Model training completed.")
    
    model_path = config["output"]["model_path"]
    dump(model, model_path)
    logging.info(f"Trained model saved to: {model_path}")
    
    return model, X_test, y_test
