import streamlit as st

from backend.connector import process_query
from utils.legal_categories import LEGAL_CATEGORIES

st.set_page_config(
    page_title="Legal Assistance",
    page_icon="⚖️",
    layout="wide"
)

st.title("⚖️ Legal Assistance")

st.markdown(
"""
Describe your legal issue.

SAHAYAK will:

- Understand your problem
- Retrieve official legal information
- Suggest required documents
- Suggest the relevant authority
"""
)

st.divider()

# -------------------------------------------------------
# Category Selection
# -------------------------------------------------------

category = st.selectbox(

    "Select Legal Category",

    list(LEGAL_CATEGORIES.keys())

)

info = LEGAL_CATEGORIES[category]

st.info(info["overview"])

# -------------------------------------------------------
# User Query
# -------------------------------------------------------

user_query = st.text_area(

    "Describe your situation",

    height=220,

    placeholder="""
Example:

My employer has not paid my salary
for four months.
"""
)

submit = st.button(

    "⚖ Get Legal Assistance",

    use_container_width=True

)

# -------------------------------------------------------
# Run AI Pipeline
# -------------------------------------------------------

if submit:

    if not user_query.strip():

        st.warning(

            "Please describe your legal issue."

        )

    else:

        with st.spinner(

            "Analyzing your request..."

        ):

            result = process_query(

                category,

                user_query

            )

        st.success(

            "Legal guidance generated successfully."

        )

        st.divider()

        # -------------------------------------

        st.subheader("📂 Case Summary")

        st.write(

            result["case_summary"]

        )

        # -------------------------------------

        st.subheader(

            "📚 Legal Information"

        )

        st.write(

            result["legal_information"]

        )

        # -------------------------------------

        st.subheader(

            "📄 Required Documents"

        )

        docs = result["required_documents"]

        if docs:

            for doc in docs:

                st.success(doc)

        else:

            st.info(

                "No documents identified."

            )

        # -------------------------------------

        st.subheader(

            "🏛 Government Authorities"

        )

        auth = result["government_authorities"]

        if auth:

            for a in auth:

                st.success(a)

        else:

            st.info(

                "No authority identified."

            )

        # -------------------------------------

        st.subheader(

            "➡ Next Steps"

        )

        st.write(

            result["next_steps"]

        )

        # -------------------------------------

        st.subheader(

            "📚 Sources"

        )

        src = result["sources"]

        if src:

            for s in src:

                st.write("•", s)

        else:

            st.info(

                "No sources available."

            )

        st.divider()

        st.warning(
"""
### ⚠ Responsible AI Disclaimer

This system provides informational guidance based on official legal resources.

It does not replace a lawyer or government authority.
"""
)