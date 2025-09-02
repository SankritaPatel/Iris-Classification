from sklearn.metrics import accuracy_score
from logger import logging

def evaluate(model, X_test, y_test):
    logging.info("Starting evaluation...")
    y_predict = model.predict(X_test)
    acc = accuracy_score(y_test, y_predict)
    logging.info(f"Model Accuracy: {acc:.4f}")
    return acc
