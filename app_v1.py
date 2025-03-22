import streamlit as st
import requests

# Backend API URL (Replace with your FastAPI URL)
API_URL = "https://web-production-48b35.up.railway.app/analyze_candidate/"

st.title("📄 AI Resume Analyzer")
st.write("Upload your resume and let AI analyze it!")

# Upload Resume (PDF)
uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

if uploaded_file:
    st.success("✅ Resume Uploaded Successfully!")

    if st.button("Analyze Resume"):
        with st.spinner("Analyzing..."):
            files = {"resume": (uploaded_file.name, uploaded_file.getvalue(), "application/pdf")}  # Fix format
            response = requests.post(API_URL, files=files)

            if response.status_code == 200:
                result = response.json()
                st.subheader("📊 Analysis Report")
                st.json(result)  # Display structured analysis
            else:
                st.error(f"❌ Failed to analyze the resume. Error: {response.text}")
