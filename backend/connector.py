"""
Connector

Connects the Streamlit frontend with the AI backend.
"""

from agents.orchestrator import run_pipeline

from agents.document_agent import verify_documents
from agents.navigation_agent import suggest_authority

from utils.logger import log_query


def process_query(category, user_query):

    # ----------------------------
    # Log user request
    # ----------------------------

    log_query(category, user_query)

    # ----------------------------
    # Run AI Pipeline
    # ----------------------------

    rag_result = run_pipeline(
        category=category,
        user_query=user_query
    )

    # ----------------------------
    # Document Agent
    # ----------------------------

    documents = verify_documents(
        category=category,
        user_query=user_query,
        retrieved_chunks=rag_result.get(
            "retrieved_chunks",
            []
        )
    )

    # ----------------------------
    # Navigation Agent
    # ----------------------------

    authorities = suggest_authority(
        category=category,
        user_query=user_query,
        retrieved_chunks=rag_result.get(
            "retrieved_chunks",
            []
        )
    )

    # ----------------------------
    # Final Response
    # ----------------------------

    return {

        "case_summary":
            rag_result.get(
                "case_summary",
                ""
            ),

        "legal_information":
            rag_result.get(
                "legal_information",
                ""
            ),

        "required_documents":
            documents,

        "government_authorities":
            authorities,

        "next_steps":
            rag_result.get(
                "next_steps",
                "Please contact the relevant authority."
            ),

        "sources":
            rag_result.get(
                "sources",
                []
            )

    }