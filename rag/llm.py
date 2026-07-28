import os

from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()


def get_llm():

    api_key = os.getenv("GOOGLE_API_KEY")

    if not api_key:
        raise ValueError(
            "GOOGLE_API_KEY not found in .env"
        )

    llm = ChatGoogleGenerativeAI(

        model="gemini-3.5-flash",

        google_api_key=api_key,

        temperature=0.2

    )

    return llm


if __name__ == "__main__":

    llm = get_llm()

    response = llm.invoke("Say hello in one sentence.")

    if isinstance(response.content, list):
        print(response.content[0]["text"])
    else:
        print(response.content)