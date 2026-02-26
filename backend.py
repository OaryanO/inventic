import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain.chains.combine_documents import create_stuff_documents_chain

import warnings
warnings.filterwarnings("ignore")

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
SERPER_API_KEY = os.getenv("SERPER_API_KEY")

os.environ["USER_AGENT"] = os.getenv("USER_AGENT")

sentiment_instruction = """Analyze the passage and identify the dominant emotional tone expressed in it. Respond using only a single descriptive emotion word."""

concise_brief_instruction = """Read the provided content and produce a clear and concise summary capturing the key ideas within two to three sentences."""

def build_llm():
    return ChatGroq(
        model="llama-3.1-8b-instant",
        api_key=GROQ_API_KEY
    )

def generate_brief(text):
    llm = build_llm()
    messages = [
        SystemMessage(content=concise_brief_instruction),
        HumanMessage(content=text)
    ]
    response = llm.invoke(messages)
    return response.content

def infer_sentiment(text):
    llm = build_llm()
    messages = [
        SystemMessage(content=sentiment_instruction),
        HumanMessage(content=text)
    ]
    response = llm.invoke(messages)
    return response.content

def identify_source(text):
    llm = build_llm()

    attribution_prompt = [
    SystemMessage(content="""
            You are a literary attribution assistant.

            Return ONLY 3 possible book matches.

            STRICT RULES:
            - No explanations
            - No reasoning
            - No additional text
            - No introduction
            - No justification
            - No extra sentences

            Output format must be EXACTLY:

            1. Book Name - Author
            2. Book Name - Author
            3. Book Name - Author

            If unsure, still provide best stylistic guesses.
            Do NOT add anything else.
            """),
    HumanMessage(content=text)
]

    try:
        response = llm.invoke(attribution_prompt).content.strip()
        return response
    except Exception:
        return "Possible sources could not be determined."


def compute_word_volume(text):
    return len(text.split())
