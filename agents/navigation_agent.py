from utils.authorities_mapping import AUTHORITIES


def suggest_authority(
    category,
    user_query=None,
    retrieved_chunks=None
):
    """
    Returns relevant government authorities.
    """

    return AUTHORITIES.get(
        category,
        ["District Legal Services Authority"]
    )