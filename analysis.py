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
    response=model.generate_content(f'''Act as an HR or Ops Head and compare the following resume with the job description. Provide:
        1. {check}
        2. {chance}
        3. {resume_tailoring}
        
        Resume: {resume_text}
        Job Description: {job_desc}
        ''')
    
    return(st.write(response.text))
    
    