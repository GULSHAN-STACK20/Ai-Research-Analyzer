# 📄 AI Research Paper Analyzer

👨‍💻 Developed by **Gulshan Kotiya**

---

## 🚀 Overview

This project is an AI-powered Research Paper Analyzer that uses a multi-agent architecture to automatically analyze, summarize, and extract insights from academic research papers.

It helps researchers and students quickly understand complex papers without reading the entire document.

---

## 🧠 Key Features

- 🔍 Extracts problem statement, methodology, and key findings
- 🧠 Generates a 150–200 word executive summary
- 📚 Extracts citations and references
- 💡 Provides practical insights and takeaways
- 🔁 Review Agent with retry logic for quality control
- 📊 Real-time progress tracking UI using Streamlit
- ⚡ Powered by OpenRouter (LLaMA / Mistral models)

---

## 🏗️ Architecture

This project follows a **multi-agent system design**:

- **Boss Agent (Pipeline Controller)**  
  Orchestrates the entire workflow

- **Sub Agents:**
  - Analyzer Agent
  - Summary Agent
  - Citation Agent
  - Insights Agent

- **Review Agent:**
  - Evaluates outputs (score 1–10)
  - Triggers retry if quality is low

---

## 🔄 Workflow

1. Upload research paper (PDF)
2. Extract text using pdfplumber
3. Analyzer Agent processes paper
4. Review Agent validates output
5. Summary, Citation, and Insights agents run
6. Final research brief is generated

---

## 🖥️ Tech Stack

- Python
- Streamlit (UI)
- OpenRouter API (LLMs)
- pdfplumber (PDF parsing)
- dotenv (environment management)

---

## 📦 Installation

```bash
git clone https://github.com/your-username/ai-research-analyzer.git
cd ai-research-analyzer
pip install -r requirements.txt
