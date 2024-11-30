import joblib
import numpy as np

# Load the trained model
model = None

def load_model():
    global model
    if model is None:
        model = joblib.load('BC_predict/breast_cancer_model.joblib')

def predict(features):
    load_model()  # Ensure the model is loaded before prediction
    features_array = np.array(features).reshape(1, -1)
    prediction = model.predict(features_array)
    return 'Malignant' if prediction[0] == 0 else 'Benign'
