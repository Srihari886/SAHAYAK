from rag.llm import get_llm
from rag.retriever import get_retriever
from prompts.prompts import LEGAL_PROMPT

llm = get_llm()
retriever = get_retriever()


def get_legal_guidance(user_query: str):

    docs = retriever.invoke(user_query)

    context = "\n\n".join(
        doc.page_content for doc in docs
    )

    prompt = f"""
{LEGAL_PROMPT}

Retrieved Legal Context:

{context}

User Query:
{user_query}
"""

    response = llm.invoke(prompt)

    return {
        "context": context,
        "legal_response": response.content
    }