from agents import run_pipeline                                                                     
import pdfplumber
import time
import streamlit as st 
st.set_page_config(page_title="AI Research Analyzer", layout="wide")


st.markdown("""
<div style="text-align: center;">
    <h1>🤖 AI Research Analyzer</h1>
    <h4>Multi-Agent System for Academic Paper Analysis</h4>
    <p><b>Analyze • Summarize • Extract • Insights</b></p>
    <p>👨‍💻 Developed by <b>Gulshan Kotiya</b></p>
</div>
""", unsafe_allow_html=True)
uploaded_file = st.file_uploader("Upload Research Paper (PDF)", type="pdf")


# -------- PDF EXTRACTOR --------
def extract_text(pdf_file):
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text


if uploaded_file:
    st.success("File uploaded successfully!")

    if st.button("Analyze Paper"):

        # ✅ DEFINE FIRST
        progress_bar = st.progress(0)
        status_text = st.empty()

        # NOW USE IT

        # Step 1
        status_text.text("🔄 Extracting PDF text... (10%)")
        progress_bar.progress(10)
        time.sleep(1)
        text = extract_text(uploaded_file)

        # Step 2
        status_text.text("🔄 Running Analyzer Agent... (30%)")
        progress_bar.progress(30)
        time.sleep(1)

        # Step 3
        status_text.text("🔄 Generating Summary... (50%)")
        progress_bar.progress(50)
        time.sleep(1)

        # Step 4
        status_text.text("🔄 Extracting Citations... (70%)")
        progress_bar.progress(70)
        time.sleep(1)

        # Step 5
        status_text.text("🔄 Generating Insights... (90%)")
        progress_bar.progress(90)
        time.sleep(1)

        # Final
        result = run_pipeline(text)

        status_text.text("✅ Completed! (100%)")
        progress_bar.progress(100)

        st.subheader("📊 Research Brief")
        st.text_area("", result, height=500)