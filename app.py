from dotenv import load_dotenv
load_dotenv() #Activate the local env Variables

import streamlit as st
import os
import google.generativeai as genai

#setup the local environment for the google API key
genai.configure(api_key = os.getenv('GOOGLE-API-KEY'))

#Gen AI model
model = genai.GenerativeModel('gemini-pro')

#Function to generate the content
def generate(query):
    response = model.generate_content(query)
    return response.text

###### Streamlit Webpage #######
st.set_page_config(page_title='LLM QnA Application')
st.header('Generating Answers using Gemini Pro')

# streamlit run app.py

input = st.text_input(label='Ask the Question', key='input')
submit = st.button(label = 'Generate Response')

if submit:
    response = generate(input)
    st.subheader('The Response is: ')
    st.write(response)