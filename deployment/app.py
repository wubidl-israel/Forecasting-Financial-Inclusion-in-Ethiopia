"""Contains code for building and deploying the app"""
import streamlit as st
import pandas as pd
import numpy as np
from utils import get_options
from prediction import predict

# get the options for the categorical variables
cat_options = get_options()


st.title("Predicting Financial Inclusion in Africa")
st.write("To predict a person whether a person is likely to have a bank account, enter their details:")
# st.text("Country")
country = st.selectbox("Country", cat_options['country'])
# st.text("Year")
year = st.selectbox("Year", np.arange(2016, 2024, 1))
# st.text("Location")
location_type = st.selectbox("Location Type", cat_options['location_type'])
# st.text("Cellphone Access")
cellphone_access = st.radio("Cellphone Access", cat_options['cellphone_access'])
# st.text("Household Size")
household_size = st.slider("Household Size", 1, 30, 1)
# st.text("Age")
age_of_respondent = st.number_input("Age", 10, 110)
# st.text("Gender")
gender_of_respondent = st.radio("Gender", cat_options['gender_of_respondent'])
# st.text("Relationship with Head of Household")
relationship_with_head = st.selectbox("Relationship with Head of Household", cat_options['relationship_with_head'])
# st.text("Marital Status")
marital_status = st.selectbox("Marital Status", cat_options['marital_status'])
# st.text("Level of Education")
education_level = st.selectbox("Level of Education", cat_options['education_level'])
# st.text("Type of Job")
job_type = st.selectbox("Type of Job", cat_options['job_type'])

# gather input into dataframe
data = pd.DataFrame(
                {
                    'country': [country],
                    'year': [year],
                    'location_type': [location_type],
                    'cellphone_access': [cellphone_access],
                    'household_size': [household_size],
                    'age_of_respondent': [age_of_respondent],
                    'gender_of_respondent': [gender_of_respondent],
                    'relationship_with_head': [relationship_with_head],
                    'marital_status': [marital_status],
                    'education_level': [education_level],
                    'job_type': [job_type],
                    'uniqueid': ['uniqueid_0'] # an arbitrary uniqueid
                }
            )

if st.button("Predict Financial Inclusion"):
    result = predict(data)
    st.text(result)
