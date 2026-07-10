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
    search_type="mmr",
    search_kwargs={
        "k": 6,
        "fetch_k": 20,
    },
)

    return retriever


if __name__ == "__main__":

    retriever = get_retriever()

    query = "My employer has not paid my salary."

    docs = retriever.invoke(query)

    print("=" * 80)

    for i, doc in enumerate(docs, start=1):

        print(f"\nDocument {i}\n")

        print(doc.page_content[:700])

        print("\n" + "=" * 80)