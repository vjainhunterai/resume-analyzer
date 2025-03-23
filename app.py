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
                ranked_results = response.json()["ranked_resumes"]
                if not ranked_results:
                    st.warning("⚠ No resumes were ranked. Please check your input files.")
                else:
                    st.subheader("🏆 Resume Ranking Results")
                     for i, candidate in enumerate(ranked_results, start=1):
                         st.markdown(f"### 🏆 Rank #{i}: {candidate['Filename']}")
                         st.write(f"**📂 Category:** {candidate['Category']}")
                         st.write(f"**📅 Experience:** {candidate['Experience_Years']} years")
                         st.write(f"**🎯 Key Skills:** {', '.join(candidate['Key_Skills'])}")
                         st.write(f"**🎓 Education:** {candidate['Education']}")
                         st.write(f"**📜 Certifications:** {', '.join(candidate['Certifications']) if candidate['Certifications'] else 'None'}")
                         st.write(f"**📊 Rank Score:** {round(candidate['Rank_Score'], 2)}")
                         st.markdown("---")  # Separator

                
            else:
                st.error(f"❌ Failed to analyze resumes. Error: {response.text}")
