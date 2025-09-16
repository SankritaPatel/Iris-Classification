from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load model from pickle file
with open('models/model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data from form
        sepal_length = float(request.form['sepal_length'])
        sepal_width = float(request.form['sepal_width'])
        petal_length = float(request.form['petal_length'])
        petal_width = float(request.form['petal_width'])

        # Model expects a 2D array
        input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
        prediction = model.predict(input_data)

        # Map label to class name
        label_map = {
            0: 'setosa',
            1: 'versicolor',
            2: 'virginica'
        }
        predicted_class = label_map.get(prediction[0], "Unknown")

        return render_template('index.html', prediction_text=f'Predicted Iris species: {predicted_class}')
    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: {str(e)}')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

