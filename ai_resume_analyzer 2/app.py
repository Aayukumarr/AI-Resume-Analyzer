import sys
import os
import re
import io

# Fallback: If run with system python where dependencies aren't installed,
# automatically locate and re-run with the virtual environment python
try:
    import streamlit as st
except ModuleNotFoundError:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    candidates = [
        os.path.join(script_dir, ".venv", "bin", "python"),
        os.path.join(script_dir, "ai_resume_analyzer 2", ".venv", "bin", "python"),
        os.path.join(os.path.dirname(script_dir), ".venv", "bin", "python"),
        os.path.join(os.path.dirname(script_dir), "ai_resume_analyzer 2", ".venv", "bin", "python"),
    ]
    venv_python = next((p for p in candidates if os.path.isfile(p) and os.access(p, os.X_OK)), None)
    if venv_python:
        os.execv(venv_python, [venv_python] + sys.argv)
    else:
        print("\n[ERROR] Streamlit is not installed in the current Python environment.")
        print("Please activate your virtual environment:\n    source .venv/bin/activate\n")
        sys.exit(1)

# Auto-launch Streamlit if run directly with `python app.py` instead of `streamlit run app.py`
if __name__ == "__main__" and not st.runtime.exists():
    from streamlit.web import cli as stcli
    sys.argv = ["streamlit", "run", sys.argv[0]]
    sys.exit(stcli.main())

try:
    import pymupdf as fitz
except ImportError:
    import fitz

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="AI Resume Analyzer", page_icon="📄", layout="wide")

st.markdown("""
<style>
.main {background-color: #f7f8fc;}
.block-container {padding-top: 2rem; max-width: 1100px;}
.hero {padding: 1.6rem; border-radius: 18px; background: linear-gradient(120deg,#152238,#315b91); color: white;}
.metric-card {padding: 1rem; border-radius: 14px; background: white; border: 1px solid #e7eaf1;}
.small-note {color: #626b7a; font-size: .9rem;}
</style>
""", unsafe_allow_html=True)

SKILL_GROUPS = {
    "Programming": ["python", "java", "c++", "c", "c#", "javascript", "typescript", "sql", "r", "go", "rust", "php", "ruby", "swift", "kotlin"],
    "Web Development": ["html", "css", "react", "angular", "vue", "next.js", "node.js", "nodejs", "express", "streamlit", "flask", "django", "fastapi", "rest api"],
    "AI / Machine Learning": ["machine learning", "deep learning", "artificial intelligence", "scikit-learn", "sklearn", "tensorflow", "pytorch", "nlp", "computer vision", "pandas", "numpy", "keras", "hugging face", "llm", "genai", "prompt engineering"],
    "Data & Tools": ["excel", "power bi", "tableau", "git", "github", "docker", "kubernetes", "aws", "azure", "gcp", "mysql", "mongodb", "postgresql", "redis", "linux", "jira"],
    "Core CS": ["data structures", "algorithms", "oop", "operating systems", "dbms", "computer networks", "system design"]
}

def extract_pdf_text(uploaded_file):
    data = uploaded_file.getvalue()
    doc = fitz.open(stream=data, filetype="pdf")
    if doc.is_encrypted:
        doc.close()
        raise ValueError("The uploaded PDF is password protected or encrypted. Please upload an unencrypted PDF.")
    pages = [page.get_text("text") for page in doc]
    doc.close()
    return "\n".join(pages).strip()

def normalize(text):
    return re.sub(r"\s+", " ", text.lower()).strip()

def find_skills(text):
    text_norm = normalize(text)
    found = []
    for skills in SKILL_GROUPS.values():
        for skill in skills:
            pattern = r"(?<![a-z0-9+#])" + re.escape(skill.lower()) + r"(?![a-z0-9+#])"
            if re.search(pattern, text_norm):
                found.append(skill)
    return sorted(set(found))

def match_score(resume_text, job_text):
    try:
        vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1, 2))
        matrix = vectorizer.fit_transform([resume_text, job_text])
        return round(float(cosine_similarity(matrix[0:1], matrix[1:2])[0][0]) * 100)
    except ValueError:
        try:
            vectorizer = TfidfVectorizer(ngram_range=(1, 1))
            matrix = vectorizer.fit_transform([resume_text, job_text])
            return round(float(cosine_similarity(matrix[0:1], matrix[1:2])[0][0]) * 100)
        except Exception:
            return 0

st.markdown("""
<div class="hero">
  <h1>📄 AI Resume Analyzer</h1>
  <p>Compare your resume with a job description, identify relevant skills, and find ways to improve.</p>
</div>
""", unsafe_allow_html=True)

st.write("")
left, right = st.columns([1, 1], gap="large")

with left:
    st.subheader("1. Upload your resume")
    resume_file = st.file_uploader("Choose a PDF resume", type=["pdf"])
    st.caption("PDF only • For scanned/image-only PDFs, text extraction may not work.")

with right:
    st.subheader("2. Add job description")
    job_description = st.text_area(
        "Paste the job description here",
        height=210,
        placeholder="Example: We are looking for a Python developer with SQL, machine learning, Git, and communication skills..."
    )

analyze = st.button("🔍 Analyze Resume", type="primary", use_container_width=True)

if analyze:
    if not resume_file:
        st.error("Please upload your resume PDF first.")
    elif not job_description.strip():
        st.error("Please paste a job description first.")
    else:
        try:
            resume_text = extract_pdf_text(resume_file)
            if len(resume_text) < 30:
                st.error("Could not extract enough text. If your PDF is scanned, try a text-based PDF.")
            else:
                score = match_score(resume_text, job_description)
                resume_skills = set(find_skills(resume_text))
                job_skills = set(find_skills(job_description))
                matched = sorted(resume_skills & job_skills)
                missing = sorted(job_skills - resume_skills)
                resume_words = len(re.findall(r"\b[\w+#.-]+\b", resume_text))
                sections = {
                    "Education": ["education", "university", "college", "degree", "b.tech", "bachelor"],
                    "Experience": ["experience", "internship", "employment"],
                    "Projects": ["projects", "project"],
                    "Skills": ["skills", "technical skills"],
                    "Certifications": ["certification", "certifications", "certificate"]
                }
                resume_lower = normalize(resume_text)
                present_sections = [name for name, terms in sections.items() if any(term in resume_lower for term in terms)]
                absent_sections = [name for name in sections if name not in present_sections]

                st.divider()
                st.subheader("Analysis Results")
                c1, c2, c3 = st.columns(3)
                c1.metric("Job Match Score", f"{score}%")
                c2.metric("Skills Matched", len(matched))
                c3.metric("Resume Word Count", f"{resume_words:,}")

                st.progress(score / 100)
                if score >= 70:
                    st.success("Strong text similarity. Review the skills gap below before applying.")
                elif score >= 40:
                    st.info("Moderate text similarity. Tailor your resume to the job description.")
                else:
                    st.warning("Low text similarity. Check whether this role matches your background.")

                a, b = st.columns(2)
                with a:
                    st.markdown("#### ✅ Skills found in both")
                    if matched:
                        st.write(", ".join(matched))
                    else:
                        st.write("No overlapping skills detected from the built-in skill list.")
                with b:
                    st.markdown("#### 🎯 Skills mentioned in job, not found in resume")
                    if missing:
                        st.write(", ".join(missing))
                    else:
                        st.write("No missing skills detected from the built-in skill list.")

                st.markdown("#### 🧩 Resume section check")
                st.write("**Sections detected:** " + (", ".join(present_sections) if present_sections else "None detected"))
                if absent_sections:
                    st.write("**Consider adding (if relevant):** " + ", ".join(absent_sections))

                st.markdown("#### 💡 Suggestions")
                suggestions = []
                if missing:
                    suggestions.append("If you genuinely have these skills, add evidence of them in your skills or project sections: " + ", ".join(missing[:8]) + ".")
                if "Projects" not in present_sections:
                    suggestions.append("Add 2–3 relevant projects with your contribution, tools used, and measurable outcomes.")
                if "Experience" not in present_sections:
                    suggestions.append("If you have internships, volunteering, or practical work, describe it clearly. Do not invent experience.")
                if "Skills" not in present_sections:
                    suggestions.append("Add a concise technical skills section grouped by category.")
                suggestions.append("Use action verbs and quantify outcomes where truthful (for example, processing time reduced by 20%).")
                suggestions.append("Customize the resume for each role; this score is a text-similarity estimate, not a hiring prediction.")
                for item in suggestions:
                    st.write("• " + item)

                with st.expander("Preview extracted resume text"):
                    st.text(resume_text[:10000] + ("..." if len(resume_text) > 10000 else ""))
                st.caption("Privacy note: this demo analyzes the uploaded file during the current app session. Avoid uploading sensitive personal data to public deployments.")
        except Exception as exc:
            st.error(f"Could not analyze this PDF: {exc}")

st.divider()
st.markdown('<p class="small-note">Mini project demo • TF-IDF + cosine similarity • Skill keyword matching • Not a real hiring or ATS guarantee</p>', unsafe_allow_html=True)
