from sklearn.ensemble import RandomForestClassifier
from logger import logging

def build_model(config):
    logging.info("Building RandomForestClassifier model...")
    
    params = config["model"]["params"]
    logging.info(f"Model parameters: {params}")
    
    model = RandomForestClassifier(**params)
    logging.info("Model instance created successfully.")
    
    return model
