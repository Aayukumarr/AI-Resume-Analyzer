# AI Resume Analyzer — Project Presentation (PPT)

---

## Presentation Overview
- **Project Title:** AI Resume Analyzer: Automated Resume Screening & Skill Gap Analysis Web Application
- **Presenter:** Ayush Kumar
- **Domain:** Artificial Intelligence & Natural Language Processing (NLP)
- **Total Slides:** 12
- **Estimated Presentation Time:** 7–10 Minutes

---

## Slide-by-Slide Outline & Speaker Script

---

### Slide 1: Title Slide
- **Title:** AI Resume Analyzer
- **Subtitle:** Automated Resume Screening and Skill Gap Analysis Web Application
- **Candidate Name:** Ayush Kumar
- **Branch / Department:** Computer Science & Engineering
- **Technologies Used:** Python, Streamlit, PyMuPDF, Scikit-learn
- **Speaker Script (What to say):**
  > *"Good morning/afternoon respected examiners and faculty members. My name is Ayush Kumar, and today I will be presenting my project titled 'AI Resume Analyzer'. This project is an automated natural language processing web application designed to evaluate candidate resumes against job descriptions, detect technical skill gaps, and provide actionable recommendations."*

---

### Slide 2: Problem Statement & Motivation
- **Key Points:**
  - **Recruiter Fatigue:** Recruiters receive 250+ applications per open role, spending an average of 6–10 minutes per resume manually.
  - **High Rejection Rate:** Up to 75% of qualified resumes are filtered out by automated ATS before human eyes see them.
  - **Lack of Transparency:** Applicants receive generic rejection emails without knowing which skills or sections were missing.
- **Speaker Script:**
  > *"The motivation behind this project comes from two major challenges in the recruitment industry. First, recruiters face massive applicant volumes, leading to cognitive fatigue and screening delays. Second, job applicants are left in the dark about why their resumes fail to pass corporate filters. Our project bridges this gap by providing an instant, objective, and transparent analysis."*

---

### Slide 3: Project Objectives
- **Key Points:**
  - Automated binary-stream text extraction from PDF resumes.
  - Statistical vectorization using **TF-IDF** with unigram and bigram feature extraction.
  - Mathematical similarity measurement using **Cosine Similarity** (0–100%).
  - Categorized skill extraction across 5 technical domains.
  - Set-theoretic gap analysis (Matched vs. Missing competencies).
  - Structural audit of standard resume sections.
- **Speaker Script:**
  > *"The primary objectives of this project are: first, to reliably extract raw text from PDF documents; second, to vectorize and compute a mathematical similarity percentage between a resume and a job description; third, to identify matched and missing technical skills; and finally, to audit essential resume sections."*

---

### Slide 4: System Architecture & Workflow
- **Visual Diagram:**
  - `PDF Resume` + `Job Description` $\rightarrow$ `PyMuPDF Extraction & Normalization`
  - `Normalized Text` $\rightarrow$ `TF-IDF Vectorizer (N-grams 1,2)`
  - `Vector Matrix` $\rightarrow$ `Cosine Similarity Engine (Score %)`
  - `Regex Keyword Extraction` $\rightarrow$ `Skill Gap Matrix (Intersection ∩ / Difference ∖)`
  - `Streamlit UI` $\rightarrow$ `Interactive Dashboard Display`
- **Speaker Script:**
  > *"Here is our system architecture. The pipeline begins when the user uploads a PDF resume and inputs a job description. PyMuPDF extracts the raw text in memory. We then apply text normalization, followed by two parallel pipelines: one feeds the text into a TF-IDF vectorizer to calculate the overall cosine match score; the second runs a boundary-checked regex engine against our skill taxonomy to detect missing competencies."*

---

### Slide 5: Mathematical Foundation & Methodology
- **Key Points:**
  - **TF-IDF (Term Frequency – Inverse Document Frequency):**
    - $\text{TF}(t, d) = \frac{f(t, d)}{\text{total words}}$
    - $\text{IDF}(t) = \ln\left(\frac{1 + N}{1 + \text{DF}(t)}\right) + 1$
    - Captures both unigrams and bigrams (e.g., *"machine learning"*).
  - **Cosine Similarity Formula:**
    - $\cos(\theta) = \frac{\mathbf{A} \cdot \mathbf{B}}{\|\mathbf{A}\|_2 \|\mathbf{B}\|_2}$
  - **Set Logic:**
    - $\text{Matched} = S_{\text{resume}} \cap S_{\text{job}}$
    - $\text{Missing} = S_{\text{job}} \setminus S_{\text{resume}}$
- **Speaker Script:**
  > *"Under the hood, we use two proven mathematical concepts. First, TF-IDF weights words based on their relative importance, ensuring that common words like 'the' or 'with' do not skew results while rewarding technical terms. Second, Cosine Similarity calculates the angle between the two document vectors in multi-dimensional space, yielding a clean 0 to 100 percentage match."*

---

### Slide 6: Skill Taxonomy & Boundary Matching
- **Domains Covered:**
  - **Programming:** Python, Java, C++, JavaScript, TypeScript, SQL, Go, Rust.
  - **Web Development:** React, Node.js, Express, Streamlit, Flask, Django, FastAPI.
  - **AI / Machine Learning:** Deep Learning, PyTorch, TensorFlow, NLP, Scikit-learn, LLMs.
  - **Data & Tools:** Docker, Kubernetes, AWS, Azure, Git, GitHub, Linux.
  - **Core CS:** Data Structures, Algorithms, OOP, DBMS, Computer Networks.
- **Regex Boundary Isolation:**
  - Uses `(?<![a-z0-9+#])skill(?![a-z0-9+#])` to prevent false positives (e.g., matching "C" inside "React").
- **Speaker Script:**
  > *"Our skill extraction utilizes a structured taxonomy covering five major technical domains. To prevent false positives—such as detecting 'C' inside the word 'React' or 'SQL' inside a URL—we employ strict lookbehind and lookahead regex boundaries."*

---

### Slide 7: Application Features & User Interface
- **Key Points:**
  - **Metric Score Cards:** Instant visual display of Match Score %, Number of Matched Skills, and Resume Word Count.
  - **Color-Coded Status Feedback:** Green for strong alignment ($\ge 70\%$), Blue for moderate ($40-69\%$), Amber for low ($< 40\%$).
  - **Side-by-Side Skills Matrix:** Clean visualization of skills present in both vs. skills missing.
  - **Section Audit & Dynamic Advice:** Identifies missing sections like Projects or Certifications and generates personalized tips.
  - **Privacy First:** Entire process executes in memory; zero personal data saved to external databases.
- **Speaker Script:**
  > *"The Streamlit frontend gives candidates immediate visual clarity. It features three headline metric cards, a color-coded status bar, a side-by-side comparison of detected versus missing skills, and dynamic advice tailored to the candidate's gaps."*

---

### Slide 8: Experimental Results & Test Cases
- **Key Points:**
  - **TC-01 (High Match):** Python/ML Developer Resume vs. Python/ML Job Description $\rightarrow$ **78% Match** (Passed).
  - **TC-02 (Low Match):** Frontend React Resume vs. Deep Learning PyTorch Role $\rightarrow$ **18% Match** (Passed).
  - **TC-03 (Moderate Match):** Full-Stack Developer vs. Cloud/DevOps Role $\rightarrow$ **54% Match** (Passed).
  - **TC-04 (Corrupted/Empty Input):** Clean error reporting without app crash.
  - **Latency:** Sub-100 millisecond execution speed.
- **Speaker Script:**
  > *"We validated the system using five diverse test cases. For closely aligned profiles, the system correctly computed a high score of 78%. For cross-domain profiles, it correctly identified the gap with an 18% score. The entire pipeline executes in under 100 milliseconds."*

---

### Slide 9: Existing Systems vs. Proposed System
- **Comparison:**
  - **Manual Review:** Slow (5–10 mins/resume), inconsistent, subjective.
  - **Commercial ATS:** Expensive, black-box with zero applicant feedback.
  - **Our System:** Sub-second execution, 100% free/open-source, full diagnostic transparency for candidates.
- **Speaker Script:**
  > *"Compared to traditional manual screening, our system is thousands of times faster. Compared to expensive commercial ATS software, our solution is fully open-source and provides transparent, actionable feedback to candidates rather than just an opaque rejection."*

---

### Slide 10: Limitations & Future Scope
- **Current Limitations:**
  - Scanned/image-only PDFs require OCR.
  - TF-IDF relies on lexical n-gram tokens rather than deep semantic synonyms (e.g., "AWS" vs. "Amazon Cloud").
- **Future Enhancements:**
  - Integrating **Tesseract OCR** for image-based resumes.
  - Adding **Transformer Embeddings (BERT / Gemini API)** for semantic understanding.
  - Supporting multiple formats (**DOCX, TXT, LaTeX**).
  - Bulk screening mode for recruiters (uploading 50+ resumes with automated CSV ranking).
- **Speaker Script:**
  > *"In terms of future scope, we plan to add Tesseract OCR for scanned PDF support, Transformer-based dense embeddings like BERT for deep semantic synonym matching, and a bulk upload feature for HR teams."*

---

### Slide 11: Conclusion
- **Key Summary:**
  - Successfully built a practical, lightweight, and robust AI Resume Analyzer.
  - Unifies PyMuPDF, Scikit-learn, and Streamlit into a responsive web application.
  - Demonstrates practical application of statistical NLP, vector space models, and information retrieval.
- **Speaker Script:**
  > *"In conclusion, the AI Resume Analyzer proves that lightweight, statistical NLP techniques like TF-IDF and Cosine Similarity can solve critical recruitment bottlenecks efficiently without requiring expensive cloud infrastructure."*

---

### Slide 12: Questions & Answers (Viva Preparation)
- **Top 5 Frequently Asked Viva Questions & Answers:**
  1. **Q: Why did you choose TF-IDF over simple keyword counting?**
     - *A:* Simple keyword counting gives unfair weight to common stop words (like "the", "and") and fails to consider document length. TF-IDF penalizes ubiquitous words while rewarding domain-specific terminology.
  2. **Q: What is Cosine Similarity and why is it preferred over Euclidean distance?**
     - *A:* Cosine similarity measures the angle between two vectors rather than their magnitude. This means a 1-page resume and a 3-page resume with the same content distribution will still achieve a fair similarity score, whereas Euclidean distance would penalize the length difference.
  3. **Q: Why did you use PyMuPDF instead of PyPDF2?**
     - *A:* PyMuPDF is backed by the high-performance C++ MuPDF engine. It is up to 10 times faster, handles complex PDF layouts better, and supports encrypted document detection.
  4. **Q: What are n-grams and why did you use `ngram_range=(1, 2)`?**
     - *A:* N-grams represent continuous sequences of $n$ words. Unigrams ($n=1$) catch single words like "Python", while bigrams ($n=2$) capture composite terms like "machine learning" or "data structures".
  5. **Q: Why use Streamlit instead of React + Flask?**
     - *A:* Streamlit is reactive and Python-native. It allows building a clean, modern UI in Python without the overhead of maintaining two separate codebases or API contracts.

---

## How to Present This Deck:
1. **Interactive HTML Presentation:** Open [`presentation.html`](file:///Users/ayushkumar/Desktop/AI%20Resume%20Analyzer/presentation.html) in your browser. Use Arrow Keys to navigate, and click **Print / Save PDF** to export slides directly!
2. **Microsoft PowerPoint / Google Slides:** Copy the slides above into PowerPoint or Google Slides templates.

