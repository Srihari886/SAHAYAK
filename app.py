import streamlit as st


st.set_page_config(
    page_title="SAHAYAK",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)


st.title("⚖️ SAHAYAK")
st.subheader("AI Legal Navigation Assistant")

st.markdown("""
Welcome to **SAHAYAK**, an AI-powered legal navigation assistant developed as part of the IIT Mandi Himashikhar Agentic AI Capstone.

SAHAYAK helps citizens:

- 📚 Understand legal procedures
- 📄 Identify important documents
- 🏛 Navigate to the appropriate government authority
- 🤖 Access information retrieved from official legal resources

> **SAHAYAK provides informational guidance only and is not a substitute for professional legal advice.**
""")

st.divider()

st.header("Project Highlights")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Knowledge Base", "92+", "Official Legal Documents")

with col2:
    st.metric("AI Agents", "5", "Multi-Agent Architecture")

with col3:
    st.metric("Legal Domains", "10+", "Government Resources")

st.divider()

st.header("How SAHAYAK Works")

with st.container(border=True):

    st.markdown("""
### Step 1️⃣

Choose **Legal Assistance** from the sidebar.

### Step 2️⃣

Select the legal category that best matches your issue.

### Step 3️⃣

Describe your situation in your own words.

### Step 4️⃣

SAHAYAK analyzes your request using multiple AI agents and official legal resources.

### Step 5️⃣

Receive:

- Relevant legal information
- Required documents
- Appropriate authority
- Suggested next steps
""")

st.divider()


st.header("Platform Features")

feature1, feature2 = st.columns(2)

with feature1:

    st.success("📚 Official Legal Knowledge Base")

    st.success("🤖 Multi-Agent AI System")

    st.success("📄 Document Verification")

with feature2:

    st.success("🏛 Legal Navigation")

    st.success("⚖ Responsible AI")

    st.success("🔍 Retrieval-Augmented Generation (RAG)")

st.divider()


st.info(
"""
Use the sidebar to open **Legal Assistance** and begin navigating your legal issue.
"""
)
