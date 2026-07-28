from agents.case_agent import analyze_case
from agents.legal_agent import get_legal_guidance


def run_pipeline(category, user_query):

    case = analyze_case(user_query)

    legal = get_legal_guidance(user_query)

    return {

        "case_summary": case,

        "legal_information": legal["answer"],

        "retrieved_chunks": legal["retrieved_chunks"],

        "sources": legal["sources"],

        "next_steps":
            "Please contact the appropriate authority for further assistance."

    }