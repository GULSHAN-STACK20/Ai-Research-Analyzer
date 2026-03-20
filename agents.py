import os
from dotenv import load_dotenv
from openai import OpenAI, RateLimitError

# ---------------- LOAD ENV ----------------
load_dotenv()

# ---------------- OPENROUTER CLIENT ----------------
client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
    default_headers={
        "HTTP-Referer": "http://localhost",
        "X-Title": "AI Research Analyzer"
    }
)

MODEL = "meta-llama/llama-3-8b-instruct"  # fast + stable


# ---------------- ANALYZER AGENT ----------------
def analyzer_agent(text):
    prompt = f"""
You are a research paper analyst.

Extract clearly:
1. Problem Statement
2. Methodology
3. Key Findings

Text:
{text}
"""
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content


# ---------------- SUMMARY AGENT ----------------
def summary_agent(text):
    prompt = f"""
Write a clear 150-200 word executive summary including:
- Problem
- Approach
- Results

Text:
{text}
"""
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content


# ---------------- CITATION AGENT ----------------
def citation_agent(text):
    prompt = f"""
Extract all citations and references from the paper.
Format as bullet points.

Text:
{text}
"""
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content


# ---------------- INSIGHTS AGENT ----------------
def insights_agent(text):
    prompt = f"""
Give practical insights:
- Key takeaways
- Real-world applications
- Future scope

Text:
{text}
"""
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content


# ---------------- REVIEW AGENT ----------------
def review_agent(output):
    prompt = f"""
You are a strict reviewer.

Give:
- Score (1 to 10)
- Short feedback

Output:
{output}
"""
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content


# ---------------- SAFE CALL ----------------
def safe_call(agent, input_text):
    try:
        return agent(input_text)
    except RateLimitError:
        return "⚠️ API limit reached. Please retry."
    except Exception as e:
        return f"⚠️ Error: {str(e)}"


# ---------------- QUALITY CHECK ----------------
def is_good(review_text):
    try:
        # Accept only high-quality outputs
        for score in ["8", "9", "10"]:
            if score in review_text:
                return True
    except:
        pass
    return False


# ---------------- VALIDATION LOOP ----------------
def validate(agent, input_text):
    last_output = ""

    for _ in range(2):  # max 2 retries
        output = safe_call(agent, input_text)
        last_output = output

        review = safe_call(review_agent, output)

        if is_good(review):
            return output

    return last_output


# ---------------- MAIN PIPELINE ----------------
def run_pipeline(text):
    # limit input (important for speed + cost)
    text = text[:1500]

    # Step 1: Analysis
    analysis = validate(analyzer_agent, text)

    # Step 2: Other agents
    summary = validate(summary_agent, analysis)
    citations = validate(citation_agent, text)
    insights = validate(insights_agent, analysis)

    # Step 3: Final Output
    final = f"""
================ 📄 RESEARCH BRIEF ================

🔍 ANALYSIS
----------------------------------------
{analysis}

🧠 EXECUTIVE SUMMARY
----------------------------------------
{summary}

📚 CITATIONS & REFERENCES
----------------------------------------
{citations}

💡 KEY INSIGHTS
----------------------------------------
{insights}

👨‍💻 Developed by Gulshan Kotiya
==================================================
"""
    return final