import streamlit as st
import requests

# Backend API URL (FastAPI)
API_URL = "https://web-production-48b35.up.railway.app/rank_resumes/"

st.title("📄 AI Resume Ranking System")
st.write("Upload multiple resumes and let AI rank them!")

# Allow multiple PDFs to be uploaded
uploaded_files = st.file_uploader("Upload Resumes (PDF)", type=["pdf"], accept_multiple_files=True)

if uploaded_files:
    st.success(f"✅ {len(uploaded_files)} resumes uploaded successfully!")

    if st.button("Rank Resumes"):
        with st.spinner("Analyzing and ranking resumes..."):
            files = [("resumes", (file.name, file.getvalue(), "application/pdf")) for file in uploaded_files]
            response = requests.post(API_URL, files=files)

            if response.status_code == 200:
                ranked_results = response.json()
                st.subheader("🏆 Resume Ranking Results")
                st.json(ranked_results)  # Display structured ranking
            else:
                st.error(f"❌ Failed to analyze resumes. Error: {response.text}")
