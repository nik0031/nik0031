import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle
# from flasgger import Swagger
import streamlit as st

# app=Flask(__name__)
# Swagger(app)

pickle_in = open("Diabetes_pickle", "rb")
classifier = pickle.load(pickle_in)

# @app.route('/')
#def welcome():
#    return "Welcome All"

# @app.route('/predict',methods=["Get"])
def Diabetes_prediction(Diabetes):
  prediction = classifier.predict([[Diabetes]])
  print(prediction)
  return prediction

def main():
    st.sidebar.header('Diabetes Prediction')
    select = st.sidebar.selectbox('Select Form', ['Form 1'], key='1')
    if not st.sidebar.checkbox("Hide", True, key='1'):
       st.title('Diabetes Prediction(Only for females above 21years of Age)')
       name = st.text_input("Name:")
       pregnancy = st.number_input("No. of times pregnant:")
       glucose = st.number_input("Plasma Glucose Concentration :")
       bp =  st.number_input("Diastolic blood pressure (mm Hg):")
       skin = st.number_input("Triceps skin fold thickness (mm):")
       insulin = st.number_input("2-Hour serum insulin (mu U/ml):")
       bmi = st.number_input("Body mass index (weight in kg/(height in m)^2):")
       dpf = st.number_input("Diabetes Pedigree Function:")
       age = st.number_input("Age:")

    submit = st.button('Predict')

    if submit:
        prediction = classifier.predict([[pregnancy, glucose, bp, skin, insulin, bmi, dpf, age]])
        if prediction == 0:
            st.write('Congratulation',name,'You are not diabetic')
        else:
            st.write(name," we are really sorry to say but it seems like you are Diabetic.")
    
    #if __name__ == '__main__':
main()