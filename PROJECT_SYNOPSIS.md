# PROJECT SYNOPSIS

## 1. Project Title
**AI Resume Analyzer: Automated Resume Screening and Skill Gap Analysis Web Application**

---

## 2. Domain & Area
- **Domain:** Artificial Intelligence & Natural Language Processing (NLP)
- **Application Area:** HR Technology, Candidate Pre-screening & Career Assistance
- **Platform:** Web Application (Streamlit / Python)

---

## 3. Introduction & Background
In today's competitive job market, recruiters and Human Resource (HR) departments receive hundreds of resumes for every job opening. Manually screening each candidate's resume against specific job requirements is time-consuming, labor-intensive, and prone to human cognitive bias. 

Conversely, job seekers frequently struggle to gauge how well their resumes match target job descriptions before applying. The **AI Resume Analyzer** is an automated, web-based tool designed to bridge this gap. It evaluates the contextual alignment between a candidate's resume (PDF) and a target Job Description (JD), detects key technical skills, identifies missing competencies, audits essential resume sections, and provides actionable improvement recommendations.

---

## 4. Problem Statement
1. **Inefficient Manual Screening:** Reviewing resumes manually leads to significant recruitment delays and inconsistent evaluations.
2. **Lack of Candidate Feedback:** Job applicants often face automated rejections from Applicant Tracking Systems (ATS) without understanding why their profile failed to match.
3. **Keyword & Skill Blindspots:** Candidates frequently omit critical industry keywords and required technical competencies that recruiters look for.

---

## 5. Objectives
- To extract clean text content from digital PDF resumes automatically using document parsing.
- To vectorize textual data using **TF-IDF (Term Frequency – Inverse Document Frequency)** techniques.
- To compute mathematical text similarity using **Cosine Similarity** algorithms.
- To categorize and extract domain-specific technical skills across multiple specializations (Programming, AI/ML, Web Development, Core CS, Data & Cloud Tools).
- To detect skill gaps by calculating intersection and set difference between resume skills and job requirements.
- To verify the presence of standard resume sections (Education, Experience, Projects, Skills, Certifications).
- To present a clear, interactive visual dashboard with match scores, skill badges, and personalized suggestions.

---

## 6. Proposed System & Architecture
The system consists of five modular pipelines:

```
[ Upload PDF Resume ]        [ Paste Job Description ]
          │                               │
          ▼                               ▼
[ PyMuPDF Text Extraction ]      [ Text Normalization ]
          │                               │
          └───────────────┬───────────────┘
                          ▼
            [ TF-IDF Vectorization ]
            (Unigram + Bigram Analysis)
                          │
                          ▼
            [ Cosine Similarity Engine ]
            (Calculates Match Score %)
                          │
          ┌───────────────┴───────────────┐
          ▼                               ▼
[ Skill Matching & Gap Analysis ]   [ Resume Structure Audit ]
(Categorized Keyword Taxonomy)     (Checks Standard Sections)
          │                               │
          └───────────────┬───────────────┘
                          ▼
        [ Streamlit Interactive Dashboard ]
  (Metrics, Progress Bar, Gap Badges, Suggestions)
```

### Detailed Pipeline Workflow:
1. **Document Ingestion:** The user uploads a resume in PDF format and inputs the target job description text.
2. **Text Extraction:** **PyMuPDF** parses the binary stream, verifies document validity (checking for encryption/password locks), and extracts raw text page by page.
3. **Text Preprocessing & Normalization:** Cleans white spaces, removes noise, and converts characters to lowercase for uniform processing.
4. **TF-IDF Vectorization:** Constructs vector representations of both texts using unigrams and bigrams (`ngram_range=(1, 2)`) while eliminating English stopwords.
5. **Cosine Similarity Computation:** Computes the angular similarity between the two document vectors in multi-dimensional space, normalized to a percentage scale ($0\% - 100\%$).
6. **Rule-Based Skill Extraction:** Uses regular expressions with word boundary checks to identify technical skills across five categories (Programming, Web Dev, AI/ML, Data/Tools, Core CS).
7. **Gap Analysis:** Computes:
   - **Matched Skills:** $\text{Resume Skills} \cap \text{Job Skills}$
   - **Missing Skills:** $\text{Job Skills} \setminus \text{Resume Skills}$
8. **Section & Structural Verification:** Scans for standard resume headings (Education, Experience, Projects, Technical Skills, Certifications).
9. **Dashboard Presentation:** Renders real-time feedback with metrics, color-coded status badges, and prioritized advice.

---

## 7. Hardware & Software Requirements

### Software Requirements:
- **Operating System:** Cross-platform (macOS, Windows 10/11, Linux)
- **Programming Language:** Python 3.10 or newer
- **Web UI Framework:** Streamlit (>= 1.36.0)
- **PDF Extraction Engine:** PyMuPDF / fitz (>= 1.24.0)
- **Machine Learning & NLP:** scikit-learn (>= 1.5.0)
- **Text Processing:** Python Standard Library (`re`, `io`, `sys`, `os`)

### Hardware Requirements:
- **Processor:** Dual-core 2.0 GHz or higher (Intel, AMD, or Apple Silicon)
- **RAM:** Minimum 2 GB (4 GB recommended)
- **Storage:** Minimum 500 MB free space
- **Display:** Any modern web browser (Google Chrome, Mozilla Firefox, Safari, Microsoft Edge)

---

## 8. Key Features
- **Instant PDF Extraction:** Fast and lightweight text parsing from vector/text-based PDF files.
- **Contextual Match Scoring:** Unigram/bigram TF-IDF cosine similarity model provides a normalized alignment score.
- **Categorized Skill Taxonomy:** Covers modern technical stacks (Python, Machine Learning, Docker, React, AWS, SQL, etc.).
- **Visual Skill Gap Report:** Identifies matched proficiencies and flags missing requirements.
- **Resume Section Checker:** Detects missing structural sections (Projects, Experience, Certifications).
- **Extracted Text Inspector:** Expandable drawer allowing users to review the extracted text for parsing transparency.
- **Privacy First:** In-memory execution without persisting candidate personal data or resumes to external databases.

---

## 9. Limitations
- **Image-Only PDFs:** Scanned or rasterized PDF resumes require Optical Character Recognition (OCR), which is not yet integrated.
- **Contextual Semantics:** TF-IDF relies on n-gram token overlap; deep semantic context (e.g., recognizing that "supervised models" implies "machine learning") requires large language model (LLM) embeddings.
- **Editable Taxonomy:** Skill recognition depends on a predefined keyword taxonomy rather than unsupervised named-entity recognition (NER).

---

## 10. Future Enhancements
- Integration of **Tesseract OCR** for scanned and graphical image resumes.
- Semantic vector embeddings using **Sentence Transformers / BERT** or Gemini API for deep contextual understanding.
- Support for multiple document formats (**DOCX, TXT, RTF**).
- Exportable PDF / CSV evaluation report for recruiters and candidates.
- AI-powered automated bullet-point rephraser using generative AI.

---

## 11. Conclusion
The **AI Resume Analyzer** demonstrates a practical, lightweight, and effective application of Natural Language Processing and Information Retrieval techniques. By combining TF-IDF vectorization, Cosine Similarity, and regex-based taxonomy matching within an intuitive Streamlit interface, the system provides instantaneous, transparent, and actionable feedback for both job applicants and preliminary recruitment screening.

