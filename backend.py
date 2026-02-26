import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage

import warnings
warnings.filterwarnings("ignore")

# Load environment variables from .env file
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Instruction used to detect dominant emotion
emotion_prompt = """Analyze the passage and identify the dominant emotional tone expressed in it. Respond using only a single descriptive emotion word."""

# Instruction used to generate concise summary
summary_prompt = """Read the provided content and produce a clear and concise summary capturing the key ideas within two to three sentences."""


# Creates and returns Groq LLM instance
def build_llm():
    return ChatGroq(
        model="llama-3.1-8b-instant",
        api_key=GROQ_API_KEY
    )


# Generates a short summary of the given passage
def generate_brief(text):

    # Initialize language model
    llm_instance = build_llm()

    # Prepare structured messages for summarization
    message_bundle = [
        SystemMessage(content=summary_prompt),   # Instruction
        HumanMessage(content=text)               # User passage
    ]

    # Invoke model with prepared prompt
    response = llm_instance.invoke(message_bundle)

    # Return summarized output
    return response.content


# Detects primary emotion from the passage
def infer_sentiment(text):

    # Initialize language model
    llm_instance = build_llm()

    # Prepare prompt messages for emotion detection
    message_bundle = [
        SystemMessage(content=emotion_prompt),   # Emotion detection instruction
        HumanMessage(content=text)               # User passage
    ]

    # Invoke model to classify emotional tone
    response = llm_instance.invoke(message_bundle)

    # Return detected emotion
    return response.content


# Suggests three possible literary sources for the passage
def identify_source(text):

    # Initialize language model
    llm_instance = build_llm()

    # Prompt crafted to ensure structured output without explanations
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
        # Invoke model to infer likely literary sources
        response = llm_instance.invoke(attribution_prompt).content.strip()
        return response

    except Exception:
        # Graceful fallback in case model fails
        return "Possible sources could not be determined."


# Calculates total number of words in the passage
def compute_word_volume(text):

    # Split text by spaces and count tokens
    word_list = text.split()

    # Return total count
    return len(word_list)