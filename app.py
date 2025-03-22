import streamlit as st
import requests
import fitz  # PyMuPDF for PDF handling

# Backend API URL (FastAPI on Railway)
API_URL = "https://web-production-48b35.up.railway.app/"

st.title("📄 AI Resume Analyzer")
st.write("Upload your resume and let AI analyze it!")

# Upload Resume (PDF)
uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

def extract_text_from_pdf(uploaded_file):
    """Extracts text from uploaded PDF"""
    pdf_reader = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = ""
    for page in pdf_reader:
        text += page.get_text("text") + "\n"
    return text

if uploaded_file:
    st.write("✅ Resume Uploaded!")

    # Extract text from PDF
    resume_text = extract_text_from_pdf(uploaded_file)

    if st.button("Analyze Resume"):
        # Send extracted text to FastAPI backend
        response = requests.post(f"{API_URL}/analyze", json={"resume_text": resume_text})

        if response.status_code == 200:
            result = response.json()
            st.subheader("📊 Analysis Report")
            st.json(result)  # Display structured analysis
        else:
            st.error("❌ Failed to analyze the resume. Try again.")
