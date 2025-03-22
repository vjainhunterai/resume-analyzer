import streamlit as st
import requests
import fitz  # PyMuPDF for PDF processing

# Llama API Details
LLAMA_API_URL = "https://your-llama-api-endpoint.com"
LLAMA_API_KEY = ""

from fastapi import FastAPI, UploadFile, File
import requests
import os

app = FastAPI()

# Use Hugging Face Llama API
HF_API_URL = "https://api-inference.huggingface.co/models/meta-llama/llama-3-8b"
HF_API_KEY = "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"

@app.post("/analyze_candidate/")
async def analyze_candidate(resume: UploadFile = File(...)):
    """Upload and analyze resume using Hugging Face API"""
    
    # Read resume text
    resume_text = await resume.read()
    resume_text = resume_text.decode("utf-8")

    # Call Hugging Face API
    response = requests.post(
        HF_API_URL,
        headers={"Authorization": f"Bearer {HF_API_KEY}"},
        json={"inputs": f"Analyze this resume: {resume_text}"}
    )

    return response.json()

