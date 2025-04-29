import streamlit as st
from time import sleep
from stqdm import stqdm
import pandas as pd
from transformers import pipeline
import json
import spacy
import spacy_streamlit

# Cached function for resource-intensive model loading
@st.cache_resource
def load_ner_model():
    try:
        return spacy.load("en_core_web_sm")
    except Exception as e:
        st.error(f"Failed to load spaCy model: {e}")
        st.stop()

# Sidebar content
def draw_sidebar():
    st.sidebar.write(
        """
        # NLP WEB APP

        This sidebar offers navigation and instructions for using the app.

        ### Features
        1. Text Summarization
        2. Named Entity Recognition
        3. Sentiment Analysis
        4. Question Answering
        5. Text Completion
        """
    )

def main():
    # Apply CSS for the animated background with an image
   
    st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://argetek.ai/images/parallax/services/services.webp');
        background-size: cover;
        background-position: center;
        height: 100vh;
        filter: contrast(130%) brightness(80%) 
    }
    </style>
    """, unsafe_allow_html=True
)


    draw_sidebar()
    st.markdown(
    """
    <h1 style="font-size: 75px; text-align: center; color: #ffffff;">NATURAL LANGUAGE PROCESSING <br>WEB APP</h1>
    """, unsafe_allow_html=True
)

    
    menu = [
        "--Select--",
        "Summarizer",
        "Named Entity Recognition",
        "Sentiment Analysis",
        "Question Answering",
        "Text Completion",
    ]
    choice = st.sidebar.selectbox("Choose what you want to do!", menu)

    if choice == "--Select--":
        
        st.markdown(
    """
    <h1 style="font-size: 25px; text-align: center; color: #ffffff;"><BR>Welcome to the NLP WebApp!<BR>Select a feature from the Sidebar</h1>
    """, unsafe_allow_html=True
)
    
    elif choice == "Summarizer":
        st.subheader("Text Summarization")
        raw_text = st.text_area("Enter Text for Summarization", "")
        num_words = st.number_input("Number of Words in Summary", min_value=5, max_value=100, value=30)

        if raw_text:
            summarizer = pipeline("summarization")
            summary = summarizer(raw_text, min_length=num_words, max_length=num_words * 2)
            result = summary[0]["summary_text"]
            st.write(f"### Summary: \n{result}")

    elif choice == "Named Entity Recognition":
        st.subheader("Named Entity Recognition")
        raw_text = st.text_area("Enter Text for NER", "")
        if raw_text:
            nlp = load_ner_model()
            doc = nlp(raw_text)
            for _ in stqdm(range(50), desc="Processing..."):
                sleep(0.05)
            spacy_streamlit.visualize_ner(doc, labels=nlp.get_pipe("ner").labels)

    elif choice == "Sentiment Analysis":
        st.subheader("Sentiment Analysis")
        raw_text = st.text_area("Enter Text for Sentiment Analysis", "")
        if raw_text:
            sentiment_analysis = pipeline("sentiment-analysis")
            result = sentiment_analysis(raw_text)[0]
            st.write(f"### Sentiment: {result['label']} (Score: {result['score']:.2f})")

    elif choice == "Question Answering":
        st.subheader("Question Answering")
        context = st.text_area("Context", "")
        question = st.text_area("Question", "")
        if context and question:
            question_answering = pipeline("question-answering")
            result = question_answering(question=question, context=context)
            st.write(f"### Answer: {result['answer']}")

    elif choice == "Text Completion":
        st.subheader("Text Completion")
        raw_text = st.text_area("Enter Text to Complete", "")
        if raw_text:
            text_generation = pipeline("text-generation")
            generated_text = text_generation(raw_text, max_length=50)[0]["generated_text"]
            st.write(f"### Completed Text: {generated_text}")

if __name__ == "__main__":
    main()
