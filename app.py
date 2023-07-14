# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 15:15:28 2021

@author: deepak
"""
import streamlit as st 
from PIL import Image
import pickle
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
st.set_option('deprecation.showfileUploaderEncoding', False)
# Load the pickled model
pickle_in = open("decision_model.pkl","rb")
model=pickle.load(pickle_in)

def predict_note_authentication(UserID, Gender,Age,EstimatedSalary):
  output= model.predict([[Age,EstimatedSalary]])
  print("Purchased", output)
  if output==[1]:
    prediction="Item will be purchased"
  else:
    prediction="Item will not be purchased"
  print(prediction)
  return prediction
def main():
    st.title("Item Purchase Prediction")
    html_temp = """
   <div class="" style="background-color:blue;" >
   <div class="clearfix">           
   <div class="col-md-12">
   <center><p style="font-size:40px;color:white;margin-top:10px;">Session on Decision Tree</p></center> 
   <center><p style="font-size:30px;color:white;margin-top:10px;">Machine Learning</p></center> 
   <center><p style="font-size:25px;color:white;margin-top:10px;">Project Deployment</p></center> 
   </div>
   </div>
   </div>
   """
    st.markdown(html_temp,unsafe_allow_html=True)
    UserID = st.text_input("UserID","")
    Gender = st.selectbox('Gender',('Male', 'Female'))
    Age = st.number_input("Insert Age",18,60)
    EstimatedSalary = st.number_input("Insert salary",15000,150000)
    resul=""
    if st.button("Predict"):
      result=predict_note_authentication(UserID, Gender,Age,EstimatedSalary)
      st.success('Model has predicted {}'.format(result))
    if st.button("About"):
      st.text("Developed by Deepak Moud")
      st.text("Trainer , Machine Learning")

if __name__=='__main__':
  main()
   
