#!/bin/bash
# Convenient one-click launcher for AI Resume Analyzer
cd "$(dirname "$0")"

if [ -f ".venv/bin/streamlit" ]; then
    .venv/bin/streamlit run app.py
elif [ -f "ai_resume_analyzer 2/.venv/bin/streamlit" ]; then
    "ai_resume_analyzer 2/.venv/bin/streamlit" run "ai_resume_analyzer 2/app.py"
else
    streamlit run app.py
fi

