from rag.llm import get_llm
from rag.retriever import get_retriever
from prompts.prompts import LEGAL_PROMPT

llm = get_llm()
retriever = get_retriever()


def get_legal_guidance(user_query: str):

    docs = retriever.invoke(user_query)

    context = "\n\n".join(
        doc.page_content[:400]
        for doc in docs
    )

    prompt = f"""
{LEGAL_PROMPT}

Retrieved Legal Context:

{context}

User Query:

{user_query}
"""

    response = llm.invoke(prompt)

    # Gemini 3.5 Flash may return list content
    # Extract plain text from Gemini response
    if isinstance(response.content, list):
        answer = ""

        for part in response.content:
            if isinstance(part, dict):
                answer += part.get("text", "")
            else:
                answer += str(part)

    else:
        answer = str(response.content)

    return {
        "answer": answer,
        "sources": list(
            {
                doc.metadata.get("source", "Unknown")
                for doc in docs
            }
        ),
        "retrieved_chunks": [
            doc.page_content
            for doc in docs
        ]
    }
