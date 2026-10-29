#!/bin/bash
# One-click launcher for AI Resume Analyzer
cd "$(dirname "$0")"

if [ -f ".venv/bin/streamlit" ]; then
    .venv/bin/streamlit run app.py
elif [ -f "../.venv/bin/streamlit" ]; then
    ../.venv/bin/streamlit run app.py
else
    streamlit run app.py
fi

