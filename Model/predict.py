import pickle
import pandas as pd
import sklearn

# This assumes your directory structure is Model/model.pkl
with open('Model/model.pkl', 'rb') as f:
    model = pickle.load(f)

# MLFLOW
MODEL_VERSION = '1.7.2'

class_labels = model.classes_.tolist()

# Define the correct feature order based on your model's training data.
# This list is crucial for the model to receive data in the correct format.
FEATURE_ORDER = ['bmi', 'age_group', 'lifestyle_risk', 'city_tier', 'income_lpa', 'occupation']

def predict_output(user_input: dict):
    # Ensure the input data has the same order as the training data
    ordered_input = {key: user_input[key] for key in FEATURE_ORDER}
    
    # Create the DataFrame with the correct column order
    df = pd.DataFrame([ordered_input])
    
    # NOTE: If your model requires one-hot encoding or other pre-processing
    # for categorical features, you must add that logic here as well.
    # The current code assumes your model handles string-based categorical data,
    # or that the categorical values are pre-encoded in your `user_input`.

    predicted_class = model.predict(df)[0]
    probabilities = model.predict_proba(df)[0]
    confidence = max(probabilities)
    class_probs = dict(zip(class_labels, map(lambda x: round(x, 4), probabilities)))
    
    return {
        "predicted_output": predicted_class,
        "confidence": round(confidence, 4),
        "class_probabilities": class_probs
    }