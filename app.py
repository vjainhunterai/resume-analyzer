import streamlit as st
import requests
import fitz  # PyMuPDF for PDF processing

# Llama API Details
LLAMA_API_URL = "https://your-llama-api-endpoint.com"
LLAMA_API_KEY = "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"

st.title("📄 AI Resume Analyzer")

st.write("Upload a resume (PDF/Text), and get AI analysis!")

# Upload File
uploaded_file = st.file_uploader("Upload your resume", type=["pdf", "txt"])

if uploaded_file:
    text_data = ""

    if uploaded_file.type == "application/pdf":
        doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        text_data = "\n".join([page.get_text() for page in doc])
    else:
        text_data = uploaded_file.read().decode("utf-8")

    # Display extracted text
    st.subheader("Extracted Resume Text")
    st.text_area("Resume Content", text_data, height=250)

    if st.button("Analyze Resume"):
        with st.spinner("Analyzing..."):
            response = requests.post(
                LLAMA_API_URL,
                json={"text": text_data, "api_key": LLAMA_API_KEY}
            )

            if response.status_code == 200:
                st.success("✅ Analysis Complete!")
                st.write(response.json())
            else:
                st.error("❌ Error analyzing resume!")
