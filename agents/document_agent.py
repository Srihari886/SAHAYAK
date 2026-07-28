from utils.document_requirements import DOCUMENT_REQUIREMENTS


def verify_documents(
    category,
    user_query=None,
    retrieved_chunks=None
):
    """
    Returns the required supporting documents
    based on the selected legal category.
    """

    return DOCUMENT_REQUIREMENTS.get(category, [])