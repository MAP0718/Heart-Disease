<h1>Heart Disease Prediction — End-to-End ML Project</h1>
Overview

This project is an end-to-end heart disease risk prediction system built using Machine Learning and deployed as a REST API using Flask.

The project focuses on real-world ML practices, including:

preprocessing with pipelines

model interpretability

recall-focused threshold tuning (healthcare use case)

deployment of a trained ML pipeline

Problem Statement

Predict whether a patient is at risk of heart disease based on clinical features such as age, blood pressure, cholesterol, ECG results, etc.

In healthcare applications, false negatives are dangerous, so recall is prioritized over accuracy.

Model & Approach
Model

Logistic Regression

Chosen for:

interpretability

stable performance on structured medical data

Preprocessing

Implemented using Scikit-Learn Pipeline

Used ColumnTransformer to handle:

numerical features

categorical features

This ensures preprocessing and model logic remain consistent during training and inference.

Interpretability

Logistic Regression coefficients were analyzed to understand feature impact.

Risk-increasing features (examples):

ca

exang

Risk-reducing features (examples):

thalach

slope

This makes the model explainable and suitable for healthcare scenarios.

Threshold Tuning (Key Decision)

Instead of using the default threshold (0.5), multiple thresholds were evaluated.

Threshold	Recall	False Negatives
0.5	Lower	Higher
0.4 (chosen)	High (~0.96)	Low
0.3	Similar recall	Too many false positives

Final threshold selected: 0.4

This improves recall while keeping false positives at an acceptable level.

🚀 Deployment
What is deployed

app.py — Flask API

heart_disease_pipeline.pkl — trained pipeline (preprocessing + model)

What is NOT deployed

Jupyter Notebook (used only for training and analysis)

API Endpoint

POST /predict

Input: JSON patient data
Output: Probability and final prediction (0/1)

Example response:

{
  "probability": 0.156,
  "prediction": 0
}

Tech Stack

Python

Scikit-Learn

Pandas

Flask

Joblib
