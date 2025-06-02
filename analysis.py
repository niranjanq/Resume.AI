import google.generativeai as genai
from pdf import read_pdf
# from app import job_desc 
import streamlit as st
import os
genai.configure(api_key=os.getenv("GOOGLE-API-KEY"))
model=genai.GenerativeModel("gemini-2.0-flash")


# Read the PDF file

def profile(resume,job_desc):
    if resume is not None:
        resume_text=read_pdf(resume)
        st.sidebar.markdown("Resume has been uploaded")
    else:
        st.warning("Please upload a resume")
    check='Am i a good fit for this job?'
    chance='Chances of getting selected'
    resume_tailoring='Tailor my resume for this job'
    response=model.generate_content(f'''Act as a HR or ops head and compare {resume_text} with {job_desc}and suggest - {check},{chance},{resume_tailoring}''')
    
    return(st.write(response.text))
    
    