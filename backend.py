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

# def identify_source(text):
#     search = GoogleSerperAPIWrapper(serper_api_key=SERPER_API_KEY)

#     urls = []
#     results = search.results(text)

#     for i in results["organic"][:2]:
#         urls.append(i['link'])

#     loader = WebBaseLoader(urls)
#     docs = loader.load()

#     llm = build_llm()

#     prompt = ChatPromptTemplate.from_template(
#         "Determine the most likely literary work and its author based on the following reference material: {context}"
#     )

#     chain = create_stuff_documents_chain(llm, prompt)
#     result = chain.invoke({"context": docs})
#     return result

# def identify_source(text):
#     llm = build_llm()

#     query_prompt = [
#     SystemMessage(content="""Convert this literary passage into a distinctive search query using unique phrases, character traits, or descriptive elements that would help identify its original book."""),
#     HumanMessage(content=text)
# ]

#     query = llm.invoke(query_prompt).content.strip()

#     search = GoogleSerperAPIWrapper(serper_api_key=SERPER_API_KEY)

#     try:
#         results = search.results(query)
#     except Exception:
#         return "Source could not be identified."

#     if not results.get("organic"):
#         return "Source could not be identified."

#     urls = []
#     for i in results["organic"][:5]:
#         urls.append(i['link'])

#     loader = WebBaseLoader(urls)
#     docs = loader.load()

#     prompt = ChatPromptTemplate.from_template(
#         "Identify the most probable book and its author based on the following material: {context}"
#     )

#     chain = create_stuff_documents_chain(llm, prompt)

#     try:
#         result = chain.invoke({"context": docs})
#         return result
#     except Exception:
#         return "Source could not be confidently determined."
    
def identify_source(text):
    llm = build_llm()

    attribution_prompt = [
        SystemMessage(content="""
            You are a literary attribution assistant.

            Your task is to identify the most likely book and author of the provided passage.

            Follow this process:
            1. Check if the passage resembles a known literary quote.
            2. If recognizable, provide:
            Book Name - Author Name
            3. If unsure, say:
            Not confidently identifiable
            Respond ONLY in the format:
            <Book Name> - <Author Name>
            or
            Not confidently identifiable
            """),
        HumanMessage(content=text)
    ]

    try:
        response = llm.invoke(attribution_prompt).content.strip()
    except Exception:
        return "Source could not be identified."

    if "Not confidently identifiable" in response:
        return "Source could not be identified."

    return response


def compute_word_volume(text):
    return len(text.split())
