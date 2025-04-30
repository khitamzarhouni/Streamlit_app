import streamlit as st
import sklearn
import pandas as pd
import numpy as np
import pickle  

# Charger le modèle entraîné
with open('random_forest_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

st.title("Prédire le Churn d'un Client")

# Formulaire pour les entrées
RowNumber = st.number_input('RowNumber', 0, 9999)
CreditScore = st.number_input('CreditScore', 0, 1000)
Age = st.number_input('Age', 18, 95)
Tenure = st.number_input('Tenure', 0, 10)
Balance = st.number_input('Balance', 0.0)
NumOfProducts = st.number_input('NumOfProducts', 1, 10)

HasCrCard = st.radio('Has Credit Card?', ['Yes', 'No'])
IsActiveMember = st.radio('Is Active Member?', ['Yes', 'No'])

EstimatedSalary = st.number_input('Estimated Salary', 10.0, 99999.0)

balance_salary_ratio = st.number_input('Balance to Salary Ratio', 0.0, 1.0)
tenure_age_ratio = st.number_input('Tenure to Age Ratio', 0.0, 1.0)

Geography = st.radio('Geography', ['France', 'Germany', 'Spain'])
Gender = st.radio('Gender', ['Female', 'Male'])

submit_button = st.button("Prédire le churn du client")

# Prédiction
if submit_button:
    # Encodage des variables catégorielles
    geography_map = {'France': 0, 'Germany': 1, 'Spain': 2}
    yes_no_map = {'Yes': 1, 'No': 0}
    gender_female = 1 if Gender == 'Female' else 0
    gender_male = 1 if Gender == 'Male' else 0

    # Création du tableau des données d'entrée (en respectant l'ordre des colonnes)
    input_data = np.array([CreditScore, geography_map[Geography], Age, Tenure, Balance,
                           NumOfProducts, yes_no_map[HasCrCard], yes_no_map[IsActiveMember],
                           EstimatedSalary, gender_female, gender_male]).reshape(1, -1)

    # Faire la prédiction
    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("Le client va churner.")
    else:
        st.success("Le client va rester.")
