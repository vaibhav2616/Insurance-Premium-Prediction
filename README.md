# Insurance-Premium-Prediction
 
This project provides a comprehensive solution for predicting insurance premiums using a machine learning model. The system is built with a backend API, a prediction model, and a frontend user interface, working together to deliver accurate premium estimations based on various user inputs.

Core Components:

FastAPI Backend (app.py): The server-side component built with FastAPI. It handles API requests, providing an endpoint (/predict) where users can submit their data. It manages the flow of information between the frontend and the machine learning model, ensuring a secure and efficient process. Key features include data validation using Pydantic schemas and a health check endpoint to monitor the API's status.

Prediction Model (predict.py): This script contains the logic for the machine learning model. It loads a pre-trained model (model.pkl) and a predict_output function that takes user data as input. The model processes the data and returns a predicted insurance premium category along with confidence scores and class probabilities. The script also handles crucial data preprocessing steps to ensure the input data matches the model's training format.

Streamlit Frontend (frontend.py): A user-friendly web interface built with Streamlit. It allows users to input their data through a simple form. The frontend sends this data to the FastAPI backend and displays the returned prediction in a clear, easy-to-understand format. It also includes error handling to manage cases where the API is unreachable or returns an error.

How it Works:

The user interacts with the Streamlit frontend, providing information such as BMI, age group, lifestyle risk, and income. This data is then packaged and sent to the FastAPI backend's /predict endpoint. The backend script passes this information to the prediction model, which processes it and returns the predicted premium category. Finally, the frontend receives this prediction and displays it to the user.
