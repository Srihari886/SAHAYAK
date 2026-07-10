from agents.case_agent import analyze_case
from agents.legal_agent import get_legal_guidance


def process_query(user_query: str):

    case_analysis = analyze_case(user_query)

    legal = get_legal_guidance(user_query)

    return {
        "case_analysis": case_analysis,
        "legal_guidance": legal["legal_response"]
    }


if __name__ == "__main__":

    query = input("Describe your legal issue: ")

    result = process_query(query)

    print("\n" + "="*80)

    print("CASE ANALYSIS\n")

    print(result["case_analysis"])

    print("\n" + "="*80)

    print("LEGAL GUIDANCE\n")

    print(result["legal_guidance"])