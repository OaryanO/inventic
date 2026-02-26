# 📚 Literary Passage Analyzer

This application analyzes a literary passage and provides:

- Word count  
- Predominant emotion  
- Probable literary sources  
- Concise summary  

It is powered by **Groq + Llama-3.1-8B** using LangChain and Streamlit.

---

## ⚠️ Before You Begin

Create a `.env` file in the root directory and add your Groq API key:

GROQ_API_KEY=your_groq_api_key_here

---

## 🚀 Setup Instructions

### 1. Clone the Repository

git clone <your-repo-link>
cd <your-repo-folder>

---

### 2. Create Virtual Environment

#### Windows
python -m venv venv
venv\Scripts\activate

#### Mac / Linux
python3 -m venv venv
source venv/bin/activate

---

### 3. Install Dependencies

pip install -r requirements.txt

---

### 4. Run the Application

streamlit run frontend.py

---

## 🧠 Features

| Feature | Description |
|--------|-------------|
| Word Count | Total number of words |
| Emotion Detection | Identifies dominant tone |
| Source Attribution | Suggests 3 possible books |
| Summarization | Provides a concise overview |

---

## 🛠️ Tech Stack

- Groq (Llama-3.1-8B)
- LangChain
- Streamlit
- Python

---

## 📂 Project Structure

backend.py  
frontend.py  
requirements.txt  
.env  
README.md  

---

## ▶️ Usage

1. Enter a literary passage  
2. Click **Run Analysis**  
3. View insights instantly  

---

## 🔑 Note

Ensure your Groq API key is active.  
You can get one from:

https://console.groq.com

---

You're ready to go 🚀
