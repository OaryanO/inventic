# 📚 Literary Passage Analyzer

This application analyzes a literary passage and provides:

- Word count  
- Predominant emotion  
- Probable literary sources  
- Concise summary  

Powered by **Groq (Llama-3.1-8B)** using LangChain and Streamlit.

---

## ⚠️ Before You Begin

Create a `.env` file in the root directory and add your Groq API key:

GROQ_API_KEY=your_groq_api_key_here

---

## 🚀 Setup Instructions

### 1. Clone the Repository

Replace `<repo-url>` with your actual GitHub repo link.

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

⚠️ Do NOT copy `<repo-url>` as-is — replace it with your repo URL.

---

### 2. Create a Virtual Environment

#### Windows

python -m venv venv
venv\\Scripts\\activate

#### Mac / Linux

python3 -m venv venv
source venv/bin/activate

---

### 3. Install Dependencies

If you don’t have `requirements.txt`, create one with:

streamlit
python-dotenv
langchain
langchain-core
langchain-community
langchain-groq

Then run:

pip install -r requirements.txt

---

### 4. Create `.env` File

In the project root, create:

.env

Add:

GROQ_API_KEY=your_actual_api_key

---

### 5. Run the Application

streamlit run frontend.py

---

## 🧠 Features

| Feature | Description |
|--------|-------------|
| Word Count | Counts total words |
| Emotion Detection | Finds dominant tone |
| Source Attribution | Suggests 3 possible books |
| Summarization | Generates concise summary |

---

## 🛠️ Tech Stack

- Groq (Llama-3.1-8B)
- LangChain
- Streamlit
- Python

---

## 📂 Project Structure

backend.py        # LLM logic  
frontend.py       # Streamlit UI  
requirements.txt  # Dependencies  
.env              # API key  
README.md  

---

## ▶️ Usage

1. Paste any literary passage  
2. Click **Run Analysis**  
3. View results instantly  

---

## 🔑 Get Your Groq API Key

https://console.groq.com

---

## 👤 Author

Aryan Singh

---

## 🛠️ Troubleshooting

If cloning fails:

git --version

If Streamlit fails:

pip install --upgrade pip
pip install streamlit

---

You're ready to run 🚀
"""


print("README.md updated!")
