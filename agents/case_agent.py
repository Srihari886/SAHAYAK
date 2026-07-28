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

    # Handle Gemini 3.5 Flash response format
    if isinstance(response.content, list):

        summary = "\n".join(
            item.get("text", "")
            for item in response.content
            if isinstance(item, dict)
        )

    else:

        summary = str(response.content)

    return summary


if __name__ == "__main__":

    result = analyze_case(
        "My employer has not paid my salary for four months."
    )

    print(result)