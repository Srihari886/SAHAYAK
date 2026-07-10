import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

def get_llm():
    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        api_key=os.getenv("GOOGLE_API_KEY"),
        temperature=0.2,
    )


if __name__ == "__main__":
    llm = get_llm()

    response = llm.invoke("Say hello in one sentence.")

    print(response.content) 