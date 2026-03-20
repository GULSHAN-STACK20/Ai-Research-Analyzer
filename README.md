# 🤖 AI Research Paper Analyzer (Multi-Agent System)

👨‍💻 Developed by Gulshan Kotiya

This project is a multi-agent AI system that analyzes research papers using OpenRouter LLMs...

## 🚀 Overview
This project is an AI-powered system that analyzes research papers using a multi-agent architecture. It automates understanding of academic papers by extracting key insights, summaries, citations, and practical takeaways.

---


## 🧠 Architecture

### 🔹 Boss Agent (Orchestrator)
- Controls workflow
- Delegates tasks
- Combines outputs

### 🔹 Sub Agents
- 📊 Paper Analyzer → Extracts methodology & findings
- 📝 Summary Agent → Generates executive summary
- 📚 Citation Agent → Extracts references
- 💡 Insights Agent → Generates real-world applications

### 🔹 Review Agent (Quality Control)
- Scores output (1–10)
- Triggers retries if score < 7
- Ensures high-quality results

---

## 🔁 Workflow

1. Upload Research Paper (PDF)
2. Paper Analyzer → Review → Retry if needed
3. Summary, Citation, Insights → Review → Retry
4. Boss Agent combines final output
5. Output: Structured Research Brief

---

## 🛠 Tech Stack

- Python
- OpenAI API
- Streamlit
- pdfplumber

---

## ⚠️ Known Limitations

- OpenAI API usage may be limited due to quota restrictions
- Fallback handling is implemented for API failures

## ▶️ How to Run

```bash
pip install openai pdfplumber python-dotenv streamlit
streamlit run app.py