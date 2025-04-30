# 🌐 Textura Analysis - NLP Web App

A powerful and interactive **Natural Language Processing (NLP)** web app built with **Streamlit**, leveraging **spaCy** and **Hugging Face Transformers**. It allows users to perform common NLP tasks directly in the browser with an easy-to-use interface.

---

## ✨ Features

🔹 **Text Summarization**  
🔹 **Named Entity Recognition (NER)**  
🔹 **Sentiment Analysis**  
🔹 **Question Answering**  
🔹 **Text Completion**

---

## 🖥️ App UI

The app includes:
- An animated background for visual appeal.
- Sidebar-based navigation.
- Real-time model outputs with loading indicators.
- Highlighted NER visualization using `spacy-streamlit`.

---

## 🚀 Demo

You can try it locally by following the instructions below.

---

## 🧪 Technologies Used

| Tech | Purpose |
|------|---------|
| [Streamlit](https://streamlit.io/) | Web UI framework |
| [spaCy](https://spacy.io/) | NLP (NER, POS tagging, etc.) |
| [Hugging Face Transformers](https://huggingface.co/transformers/) | Pretrained models (summarization, sentiment, QA) |
| [stqdm](https://github.com/zhang-yangzhong/stqdm) | Progress bar in Streamlit |
| [Python](https://www.python.org/) | Backend logic |

---

## 📦 Installation

```bash
# Clone the repo
git clone https://github.com/yourusername/textura-nlp-app.git
cd textura-nlp-app

# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Download the spaCy model
python -m spacy download en_core_web_sm

# Run the app
streamlit run app.py
