import streamlit as st
import os, uuid, pandas as pd
from src.parsing import extract_text_from_pdf, extract_text_from_docx, normalize_text
from src.tfidf_engine import TFIDFEngine
from src.scoring import compute_scores
from src.explain import highlight_matches

# ===== Page Config =====
st.set_page_config(
    page_title="Smart Resume Screener ✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ===== Sidebar Info =====
st.sidebar.title("Resume Screening Agent")
st.sidebar.markdown(
    """
    This tool uses **TF-IDF similarity scoring** to screen resumes against a job description.
    
    **Features:**
    - Upload multiple resumes (PDF, DOCX, TXT)
    - Specify required skills & minimum experience
    - View scoring, justifications & skill highlights
    - Download results as CSV
    """
)

# ===== Header =====
st.title("🚀 Smart Resume Screener")
st.markdown("Match resumes efficiently against your **job description** with AI-powered scoring!")

# ===== Section 1: Job Description =====
st.subheader("1️⃣ Job Description & Requirements")
with st.expander("Paste your job description and optional requirements here"):
    jd_text = st.text_area("Job Description", height=200, placeholder="Paste job description here...")
    req_skills_input = st.text_input(
        "Required skills (comma-separated, optional)", 
        value="", 
        help="e.g., Python, Machine Learning, SQL"
    )
    required_skills = [s.strip().lower() for s in req_skills_input.split(",") if s.strip()]
    req_years = st.number_input(
        "Minimum years of experience (optional)", 
        min_value=0, max_value=50, value=0
    )

# ===== Section 2: Upload Resumes =====
st.subheader("2️⃣ Upload Resumes")
uploaded_files = st.file_uploader(
    "Upload multiple resumes (PDF, DOCX, TXT)", 
    type=["pdf", "docx", "txt"], 
    accept_multiple_files=True
)
st.info(f"Uploaded {len(uploaded_files)} file(s)" if uploaded_files else "No files uploaded yet.")

# ===== TF-IDF Engine =====
engine = TFIDFEngine()

# ===== Section 3: Run Screening =====
st.subheader("3️⃣ Run Screening")
if st.button("Run Screening ⚡"):
    if not jd_text:
        st.error("❌ Please paste a job description first.")
    elif not uploaded_files:
        st.error("❌ Please upload at least one resume file.")
    else:
        st.info("Processing resumes... Please wait ⏳")
        docs = []
        meta = []
        os.makedirs("data/temp_uploads", exist_ok=True)

        for f in uploaded_files:
            ext = f.name.split(".")[-1].lower()
            uid = str(uuid.uuid4())
            path = os.path.join("data", "temp_uploads", uid + "." + ext)

            with open(path, "wb") as fh:
                fh.write(f.getbuffer())

            # Extract text based on file type
            if ext == "pdf":
                text = extract_text_from_pdf(path)
            elif ext == "docx":
                text = extract_text_from_docx(path)
            else:
                with open(path, "r", encoding='utf-8', errors='ignore') as tf:
                    text = tf.read()

            text = normalize_text(text)
            docs.append(text)
            meta.append({"filename": f.name, "path": path})

        # Compute TF-IDF Scores
        scores = compute_scores(engine, jd_text, docs, required_skills, req_years)

        # Prepare results DataFrame
        rows = []
        for i, s in enumerate(scores):
            rows.append({
                "File": meta[i]["filename"],
                "Score": round(s["final_score"], 4),
                "Similarity": round(s["similarity"], 4),
                "Matched Skills": ", ".join(s.get("matched_skills", [])),
                "Estimated Years": s.get("years", 0),
                "Justification": s.get("justification", "")
            })

        df = pd.DataFrame(rows).sort_values("Score", ascending=False).reset_index(drop=True)
        st.success("✅ Screening Complete!")
        st.dataframe(df, use_container_width=True)

        # View individual resume justification
        if len(df) > 0:
            st.subheader("🔍 Inspect Individual Resume")
            idx = st.number_input(
                "Resume index (0-based)", 
                min_value=0, max_value=len(df) - 1,
                value=0
            )
            rec = scores[int(idx)]
            st.markdown(f"### {meta[int(idx)]['filename']} — Score: {rec['final_score']:.2f}")
            st.write("**Justification:**", rec.get("justification", "No justification available."))
            st.markdown(
                highlight_matches(rec.get("raw", "")[:5000], rec.get("matched_skill_list", [])),
                unsafe_allow_html=True
            )

        # CSV Download
        csv = df.to_csv(index=False)
        st.download_button(
            label="📥 Download Results as CSV",
            data=csv,
            file_name="resume_screening_results.csv",
            mime="text/csv"
        )

# ===== Footer =====
st.markdown("---")
st.markdown("Made with ❤️ by **Smart Resume Screener** | Powered by TF-IDF")
