import streamlit as st
import pandas as pd
from flask import Flask,request,render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData,PredictPipeline# Replace with your actual prediction pipeline import

# Assuming CustomData and get_data_as_data_frame are defined somewhere else in your codebase
class CustomData:
    def __init__(self, gender, race_ethnicity, parental_level_of_education, lunch,
                 test_preparation_course, reading_score, writing_score):
        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.reading_score = reading_score
        self.writing_score = writing_score
    
    def get_data_as_data_frame(self):
        data = {
            'gender': [self.gender],
            'race_ethnicity': [self.race_ethnicity],
            'parental_level_of_education': [self.parental_level_of_education],
            'lunch': [self.lunch],
            'test_preparation_course': [self.test_preparation_course],
            'reading_score': [self.reading_score],
            'writing_score': [self.writing_score]
        }
        return pd.DataFrame(data)

# Streamlit app code
def main():
    st.title('Predict Student\'s Math Score')

    # Input fields for user data
    st.subheader('Input Students Details')
    gender = st.selectbox('Gender', ['male', 'memale'])
    race_ethnicity = st.selectbox('Ethnicity', ['group A', 'group B', 'group C', 'group D', 'group E'])
    parental_level_of_education = st.selectbox('Parental Education', ['some high school', 'high school', 'some college', 'associate\'s degree', 'bachelor\'s degree', 'master\'s degree'])
    lunch = st.selectbox('Lunch Type', ['standard', 'free/reduced'])
    test_preparation_course = st.selectbox('Test Prep Course', ['completed', 'none'])
    reading_score = st.number_input('Reading Score', min_value=0, max_value=100, step=1)
    writing_score = st.number_input('Writing Score', min_value=0, max_value=100, step=1)

    if st.button('Predict'):
        data = CustomData(gender, race_ethnicity, parental_level_of_education, lunch,
                          test_preparation_course, reading_score, writing_score)
        pred_df = data.get_data_as_data_frame()

        predict_pipeline = PredictPipeline()  # Initialize your prediction pipeline here
        results = predict_pipeline.predict(pred_df)

        # Display results
        st.subheader('Prediction Results')
        st.write(f'The student would score : {results[0]}')  # Assuming results is a list or array containing predictions

if __name__ == '__main__':
    main()
