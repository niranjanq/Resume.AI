from dotenv import load_dotenv
load_dotenv()  # activate the local env vars

import streamlit as st
import google.generativeai as genai

from pdf import read_doc
from analysis import profile
# Create the frontend
st.header(":blue[Resume AI]", divider='green')
st.subheader("Let's analyze your resume")
st.sidebar.header("Upload your resume")
resume=st.sidebar.file_uploader(label='Upload your resume here',
                         type=['pdf'])





#  Job Description 
st.subheader("Paste the job description here",divider=True)
job_desc=st.text_area(label="Job Description",placeholder="Paste the job description here",height=300,max_chars=10000)
button=st.button(label="Analyze")
if button:
    st.markdown(profile(resume=resume,job_desc=job_desc))