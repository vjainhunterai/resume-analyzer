import streamlit as st
import requests

# Backend API URL (Replace with your FastAPI endpoint)
API_URL = "https://web-production-48b35.up.railway.app/rank_resumes/"

st.title("📄 AI Resume Ranking System")
st.write("Upload multiple resumes and get ranked analysis based on experience, skills, and certifications.")

# Upload Multiple Resumes (PDF)
uploaded_files = st.file_uploader("Upload Resumes (PDF)", type=["pdf"], accept_multiple_files=True)

if uploaded_files:
    st.success(f"✅ {len(uploaded_files)} Resumes Uploaded Successfully!")

    if st.button("Rank Resumes"):
        with st.spinner("Analyzing and Ranking Resumes..."):

            # Prepare files for API request
            files = [("resumes", (file.name, file.getvalue(), "application/pdf")) for file in uploaded_files]

            response = requests.post(API_URL, files=files)

            if response.status_code == 200:
                ranked_resumes = response.json()["Ranked_Resumes"]

                st.subheader("📊 Ranked Resume Analysis")

                # Display results in a table format
                for i, candidate in enumerate(ranked_resumes, start=1):
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
