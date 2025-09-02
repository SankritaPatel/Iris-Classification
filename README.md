# 🌼 Iris Classification Pipeline  

A simple yet modular **machine learning pipeline** to classify iris species using **scikit-learn**.  
The project is structured with configuration, logging, training, and evaluation separated into different components for better readability and maintainability.  

---

## 📁 Project Structure  

```
├── configs/
│   └── config.yaml       # Configuration Files
├── logger.py             # Logging Setup and Utilities
├── exception.py          # Custom Exception Handling 
├── main.py               # Entry Point for the Pipeline
├── src/                  # Source Code
│   ├── data_loader.py    # Data Loading and Preprocessing
│   ├── model.py          # Model Architecture and Related Functions
│   ├── train.py          # Model Training Script
│   └── evaluate.py       # Model Evaluation Logic
├── models/               # Saved Models
│   └── model.joblib
├── requirements.txt      # Project Dependencies
└── README.md
```

---

## 🔍 Problem Statement  

The goal is to build a machine learning model that accurately classifies **Iris flowers** into one of three species:  

- 🌱 Setosa  
- 🌿 Versicolor  
- 🌸 Virginica  

Classification is based on **4 features**:  
- Sepal Length  
- Sepal Width  
- Petal Length  
- Petal Width  

---

## ⚙️ Setup Instructions  

### 1. 📦 Clone the Repository  

```bash
git clone https://github.com/SankritaPatel/Iris-Classification.git
cd iris-classification-pipeline
```

### 2. 🐍 Create & Activate Virtual Environment  

#### On **Windows**  
```bash
python -m venv venv
venv\Scripts\activate
```

#### On **macOS/Linux**  
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. 🔧 Install Requirements  

```bash
pip install -r requirements.txt
```

---

## 🚀 Run the Project  

```bash
python main.py
```

---

## 📊 Output  

- Trained model is saved in the `models/` directory as `model.joblib`.  
- Logs are generated to track training and evaluation progress.  
- Evaluation metrics are displayed in the terminal.  

---

## 🤝 Contribution  

Feel free to fork the repo, open issues, and submit pull requests to enhance the pipeline 🚀.  

---

## 📜 License  

This project is licensed under the **MIT License**.  
