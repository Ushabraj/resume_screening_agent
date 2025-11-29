# 🚀 Smart Resume Screener — TF-IDF Powered

## 1️⃣ Overview
Smart Resume Screener is an AI-powered application to **screen resumes efficiently** using TF-IDF similarity scoring. It compares resumes against a job description and ranks candidates based on **skills, experience, and relevance**.

## 2️⃣ Features
- Upload multiple resumes (PDF, DOCX, TXT)
- Specify required skills and minimum years of experience
- Compute TF-IDF similarity and final score
- View detailed justifications and skill highlights
- Export results to CSV
- Inspect individual resumes

## 3️⃣ Limitations
- Cannot process scanned images (requires OCR)
- Keyword-based matching may miss semantic similarities
- Accuracy depends on the quality of the job description and resumes

## 4️⃣ Tech Stack & APIs
- **Python 3.10+**
- **Streamlit** — Web interface
- **Pandas, NumPy** — Data processing
- **Scikit-learn (TF-IDF Vectorizer)** — Scoring
- Optional: **PDF/DOCX libraries** (`PyPDF2`, `python-docx`)  

## 5️⃣ Setup & Run Instructions
1. Clone the repository:
```bash
git clone https://github.com/Ushabraj/smart-resume-screener.git
cd smart-resume-screener

pip install -r requirements.txt

streamlit run app.py
Network URL: http://192.168.43.122:8508

       ┌───────────────────────────┐
       │       Recruiter / User    │
       │ Paste JD & Upload Resumes │
       └─────────────┬────────────-┘
                     │
                     ▼
       ┌───────────────────────────┐
       │    Streamlit Interface    │
       │ - Job Description Input   │
       │ - Resume Upload           │
       │ - Skills & Experience     │
       └─────────────┬────────────-┘
                     │
                     ▼
       ┌───────────────────────────┐
       │       TF-IDF Engine       │
       │ - Text Normalization      │
       │ - TF-IDF Vectorization    │
       │ - Skill Matching          │
       │ - Experience Estimation   │
       └─────────────┬────────────-┘
                     │
                     ▼
       ┌───────────────────────────┐
       │      Scoring Module       │
       │ - Combine Scores          │
       │ - Generate Justifications │
       └─────────────┬────────────-┘
                     │
                     ▼
       ┌───────────────────────────┐
       │  Results & Export Module  │
       │ - Ranked Table            │
       │ - Skill Highlights        │
       │ - CSV Download            │
       └───────────────────────────┘

![Logo](c:\Users\USHA\Downloads\resume_screening.png)

