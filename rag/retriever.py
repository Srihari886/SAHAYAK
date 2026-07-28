from langchain_community.vectorstores import Chroma
from rag.embeddings import get_embeddings

CHROMA_DIRECTORY = "vectordb"


def get_retriever():

    embeddings = get_embeddings()

    db = Chroma(
        persist_directory=CHROMA_DIRECTORY,
        embedding_function=embeddings,
    )

    retriever = db.as_retriever(
        search_type="similarity",
        search_kwargs={
            "k": 2
        }
    )

    return retriever


if __name__ == "__main__":

    retriever = get_retriever()

    docs = retriever.invoke(
        "My employer has not paid my salary."
    )

    for i, doc in enumerate(docs):

        print("=" * 80)

        print(doc.page_content[:500])