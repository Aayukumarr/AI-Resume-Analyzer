# AI Resume Analyzer — Mini Project

A beginner-friendly resume analysis web app built with Streamlit and Python.

## Features
- Upload a text-based PDF resume
- Paste a job description
- Calculate a TF-IDF cosine-similarity score
- Find skills present in both the resume and job description
- Identify job-description skills not detected in the resume
- Check common resume sections and show improvement suggestions

## Tech stack
- Python (>= 3.10)
- Streamlit (web UI)
- PyMuPDF (PDF text extraction)
- scikit-learn (TF-IDF and cosine similarity)

## How to Run

### Method 1: One-Click Run Script (Fastest)
From the project folder in Terminal:
```bash
./run.sh
```

### Method 2: Standard Streamlit Command
1. Open Terminal in the project folder.
2. Activate the virtual environment:
   ```bash
   source .venv/bin/activate
   ```
3. Run Streamlit:
   ```bash
   streamlit run app.py
   ```
4. Open the browser URL shown (typically `http://localhost:8501`).

### Method 3: Direct Python / IDE Run Button
You can also run directly with Python or the VS Code / IDE Run button:
```bash
python3 app.py
```
*(The script will automatically detect the virtual environment and start the Streamlit web server for you).*

---

## Installing Dependencies Manually (If setting up fresh)
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## How it works
1. **PyMuPDF** extracts text from the uploaded PDF.
2. **TF-IDF** converts the resume and job description into numerical text vectors.
3. **Cosine similarity** calculates their text similarity percentage.
4. Built-in keyword matching detects common technical skills across categories.
5. The app compares detected skills and generates improvement suggestions.

## Limitations
- The match score is a text-similarity estimate, not a hiring probability or official ATS score.
- Skill detection uses a built-in keyword list in `app.py`.
- Scanned/image-only PDFs may need OCR, which is not included.
- The app does not verify whether a candidate truly has a listed skill.
