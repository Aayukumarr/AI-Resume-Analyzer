# Top 12 Most Frequently Asked Viva & Presentation Questions (With Exact Answers)

**Project Title:** AI Resume Analyzer: Automated Resume Screening & Skill Gap Analysis Web Application  
**Domain:** Natural Language Processing (NLP) & Artificial Intelligence  

---

## CATEGORY 1: Core NLP & Mathematical Concepts

### Q1. What is TF-IDF and why did you use it instead of simple Word Count (Bag of Words)?
- **Examiner's Intent:** To check if you understand information retrieval and word weighting.
- **Answer:**
  > *"Simple word counting counts every word equally. As a result, generic words like 'the', 'is', 'experience', or 'developer' get high weights simply because they repeat often.*
  > 
  > *TF-IDF (Term Frequency – Inverse Document Frequency) solves this by multiplying two factors:*
  > 1. *TF measures how often a word appears in a specific document.*
  > 2. *IDF down-weights ubiquitous words that appear across all documents and rewards rare, domain-specific keywords (like 'PyTorch', 'Kubernetes', or 'Django').*
  > 
  > *This gives a statistically accurate representation of document relevance."*

---

### Q2. Why did you use Cosine Similarity instead of Euclidean Distance?
- **Examiner's Intent:** To check if you understand vector spaces and document length normalization.
- **Answer:**
  > *"Euclidean distance measures the straight-line distance between vector points, which is heavily distorted by document length. For instance, a 1-page resume and a comprehensive 4-page resume with the exact same skills would have a large Euclidean distance, making the candidate appear unqualified.*
  > 
  > *Cosine similarity measures the **angle** between two vectors, completely independent of document magnitude:*
  > $$\cos(\theta) = \frac{\mathbf{A} \cdot \mathbf{B}}{\|\mathbf{A}\|_2 \|\mathbf{B}\|_2}$$
  > *It evaluates thematic orientation rather than length, yielding a fair $0\%$ to $100\%$ alignment score."*

---

### Q3. What are N-grams, and why did you set `ngram_range=(1, 2)`?
- **Examiner's Intent:** To test if you understand token context.
- **Answer:**
  > *"An n-gram is a continuous sequence of $n$ words.*
  > - *Unigrams ($n=1$) capture single words like 'Python', 'SQL'.*
  > - *Bigrams ($n=2$) capture two-word phrases like 'machine learning', 'deep learning', or 'data structures'.*
  > 
  > *If we only used unigrams ($n=1$), the model would treat 'machine' and 'learning' as unrelated words. Setting `ngram_range=(1, 2)` allows us to capture both individual tools and compound technical disciplines."*

---

## CATEGORY 2: Implementation & Technology Stack

### Q4. Why did you choose PyMuPDF (`fitz`) over `PyPDF2` or `pdfplumber`?
- **Examiner's Intent:** To check if you researched your libraries.
- **Answer:**
  > *"PyMuPDF is built on the high-performance C++ MuPDF rendering engine. Benchmarks show it is up to **10 to 15 times faster** than pure Python libraries like PyPDF2.*
  > 
  > *Additionally, PyMuPDF handles multi-column layouts, font encodings, and whitespace normalization with far fewer corrupted characters, and easily checks if a document is password protected via `doc.is_encrypted`."*

---

### Q5. Why did you choose Streamlit instead of React with Flask/Django?
- **Examiner's Intent:** To understand your architectural choice.
- **Answer:**
  > *"Streamlit allows us to build a reactive, production-ready data science web interface natively in Python without maintaining two separate codebases, REST API contracts, or state management frameworks.*
  > 
  > *It executes entirely in memory, provides instant reload on code updates, and ensures zero latency between the NLP processing engine and the UI components."*

---

### Q6. How does your Skill Matching work, and how do you prevent False Positives?
- **Examiner's Intent:** To check if you know how regex boundary matching works.
- **Answer:**
  > *"If you use simple string search like `if 'c' in text:`, it will match the letter 'c' inside 'React' or 'CSS'.*
  > 
  > *To prevent false positives, we use **Regular Expression boundary isolation** with lookbehinds and lookaheads:*
  > ```python
  > r"(?<![a-z0-9+#])" + re.escape(skill) + r"(?![a-z0-9+#])"
  > ```
  > *This guarantees that characters like 'C', 'C++', and 'C#' are matched only as standalone tokens, preventing partial substring matches."*

---

## CATEGORY 3: Project Workflow & Logic

### Q7. Can you explain the end-to-step pipeline from PDF upload to results?
- **Examiner's Intent:** To test your overall grasp of the project flow.
- **Answer:**
  > *"The pipeline runs in 5 clear steps:*
  > 1. *Binary PDF upload: PyMuPDF parses the document into raw string text.*
  > 2. *Text Normalization: Lowercasing and whitespace cleanup.*
  > 3. *Vectorization: TfidfVectorizer transforms the clean resume and job description into numerical sparse vectors.*
  > 4. *Cosine Similarity: Computes the dot product of normalized vectors to generate the Match Score %.*
  > 5. *Rule-Based Set Analysis: Our regex engine extracts skills across 5 domains, calculating intersection for matched skills ($S_{\text{resume}} \cap S_{\text{job}}$) and set difference for missing skills ($S_{\text{job}} \setminus S_{\text{resume}}$)."*

---

### Q8. How do you detect if standard resume sections are present or missing?
- **Examiner's Intent:** To check if you know your heuristic audit logic.
- **Answer:**
  > *"We define synonym dictionaries for 5 essential sections: Education, Experience, Projects, Skills, and Certifications. The system normalizes the resume text and searches for these heading triggers. If a section heading is absent, the system flags it and dynamically appends guidance to the suggestion list."*

---

## CATEGORY 4: Limitations & Edge Cases (Examiners' Favorite!)

### Q9. What happens if a candidate uploads a scanned image PDF (photo of a resume)?
- **Examiner's Intent:** Testing your understanding of document types and edge cases.
- **Answer:**
  > *"PyMuPDF extracts text streams embedded in digital PDFs. If a user uploads a scanned or photo-based PDF, the extracted text length will be near zero.*
  > 
  > *Our code explicitly validates this: if `len(resume_text) < 30`, it displays a friendly error stating 'Could not extract enough text; try a text-based PDF'. In future scope, we plan to integrate **Tesseract OCR** to handle scanned documents."*

---

### Q10. What if a candidate attempts 'Keyword Stuffing' (e.g. copying the whole JD in tiny white font)?
- **Examiner's Intent:** Testing critical evaluation of statistical NLP limitations.
- **Answer:**
  > *"That is a known limitation of lexical TF-IDF matching. If keywords are present in the text stream, the TF-IDF score will increase.*
  > 
  > *However, our system mitigates this in two ways: first, our **Word Count Metric** flags abnormally high text volumes; second, our **Extracted Text Drawer** allows the human recruiter to preview exactly what text was parsed, exposing hidden or duplicated text immediately."*

---

### Q11. Will your system recognize that 'AWS' and 'Amazon Web Services' are the same skill?
- **Examiner's Intent:** Testing your awareness of lexical vs. semantic search.
- **Answer:**
  > *"In the current TF-IDF model, terms are evaluated lexically, meaning exact token overlap. To handle common abbreviations, our skill taxonomy includes both forms (e.g., 'scikit-learn' and 'sklearn', 'node.js' and 'nodejs').*
  > 
  > *For universal synonym recognition, the next phase of our project involves upgrading from TF-IDF to **Transformer Dense Embeddings (like BERT or Gemini API)**, which inherently understand semantic synonyms."*

---

## CATEGORY 5: Future Scope & Real-World Applicability

### Q12. How would you scale this project for a large enterprise receiving 10,000 resumes?
- **Examiner's Intent:** Testing scalability thinking.
- **Answer:**
  > *"To scale this for enterprise use:*
  > 1. *Convert from single-file upload to **Batch Asynchronous Processing** using a queue (like Celery / Redis).*
  > 2. *Store pre-computed resume vectors in a **Vector Database** (like ChromaDB or Pinecone) for instant retrieval.*
  > 3. *Add an automated candidate ranking table with CSV export for recruiters.*
  > 4. *Integrate an LLM to generate auto-drafted personalized feedback emails to candidates."*
