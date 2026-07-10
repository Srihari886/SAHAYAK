from rag.llm import get_llm
from prompts.prompts import CASE_PROMPT

llm = get_llm()


def analyze_case(user_query: str):
    prompt = f"""
{CASE_PROMPT}

User Description:
{user_query}
"""

    response = llm.invoke(prompt)

    return response.content


if __name__ == "__main__":
    result = analyze_case(
        "My employer has not paid my salary for four months."
    )

    print(result)