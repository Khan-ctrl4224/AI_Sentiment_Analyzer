import streamlit as st
from textblob import TextBlob

st.set_page_config(page_title="AI Sentiment Analyzer", page_icon="🤖")

st.title("🤖 AI Sentiment Analyzer")
st.write("Type a sentence below and find out if it's Positive, Negative, or Neutral.")

text = st.text_area("Enter text to analyze:")

if st.button("Analyze"):
    if text.strip() == "":
        st.warning("Please enter some text.")
    else:
        blob = TextBlob(text)
        sentiment_score = blob.sentiment.polarity

        if sentiment_score > 0:
            st.success(f"Sentiment: Positive 😊 (Confidence: {sentiment_score * 100:.2f}%)")
        elif sentiment_score < 0:
            st.error(f"Sentiment: Negative 😞 (Confidence: {abs(sentiment_score) * 100:.2f}%)")
        else:
            st.info("Sentiment: Neutral 😐 (Confidence: 0%)")
