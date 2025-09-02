import sys
import yaml
from logger import logging
from exception import CustomException
from src import data_loader, model, train, evaluate


if __name__ =="__main__":
    logging.info("Starting the training pipeline...")
    try:
        # Load config
        logging.info("Loading configuration from config.yaml")
        config = yaml.safe_load(open("configs/config.yaml"))

        # Load data
        logging.info("Loading data...")
        X, y = data_loader.load_data()
        logging.info(f"Data loaded successfully. Feature shape: {X.shape}, Target shape: {y.shape}")

        # Build model
        logging.info("Building model...")
        clf = model.build_model(config=config)
        logging.info("Model built successfully.")

        # Train model
        logging.info("Starting model training...")
        clf, X_test, y_test = train.train(X, y, clf, config=config)
        logging.info("Model training completed.")

        # Evaluate model
        logging.info("Starting model evaluation...")
        evaluate.evaluate(clf, X_test, y_test)
        logging.info("Model evaluation completed.")
        
    except Exception as e:
        raise CustomException(e, sys)
