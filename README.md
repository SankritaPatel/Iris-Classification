# 🌼 Iris Classification Pipeline

A simple machine learning pipeline to classify iris species using scikit-learn. The project follows a modular structure with configuration, logging, training, and evaluation separated into different components.


## 📁 Project Structure

├── configs/
│   └── config.yaml # Configuration Files
├── logger.py # Logging Setup and Utilities
├── exception.py # Custom Exception Handling 
├── main.py # Entry point for the entire pipeline
├── src/ # Source Code
│   ├── data_loader.py # Data loading and preporcessing
│   ├── model.py # Model Architecture and related functions
│   ├── train.py # Model Training Script
│   └── evaluate.py # Model evaluation logic
├── models/  # Saved Models
│   └── model.joblib
├── README.md


## 🔍 Problem Statement

The goal is to build a machine learning model that accurately classifies Iris flowers into one of three species:
- Setosa
- Versicolor
- Virginica

The classification is based on 4 features:
- Sepal Length
- Sepal Width
- Petal Length
- Petal Width
  

## 🛠️ How to Use

### 1. 🔧 Install Requirements

```
pip install -r requirements.txt
```
### 2. 🚀 Run the Poroject

```
python main.py
```
