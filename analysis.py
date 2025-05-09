import google.generativeai as genai
from pdf import read_doc
import streamlit as st
import os
genai.configure(api_key=os.getenv("GOOGLE-API-KEY"))
model=genai.GenerativeModel("gemini-2.0-flash")


# Read the PDF file

def profile(resume,job_desc):
    if resume is not None:
        resume_text=read_doc(resume)
        st.markdown("Resume has been uploaded")
    else:
        st.warning("Please upload a resume")
    check='Am i a good fit for this job?'
    chance='Chances of getting selected'
    resume_tailoring='Tailor my resume for this job'
    response=model.generate_content('''Act as a HR or ops head in AI domain and compare {resume} with {job_desc}
and suggest - {check},{chance},{resume_tailoring}''')
    
    return(st.write(response.text))
    
    