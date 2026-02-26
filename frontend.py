import streamlit as st

from backend import generate_brief, infer_sentiment, identify_source, compute_word_volume

def app():
    st.set_page_config(page_title="Assignment", page_icon="📚", layout="centered")
    st.title("Assignment")
    st.markdown("This application evaluates a literary passage and provides analytical insights.")

    st.markdown("Paste the passage below to begin analysis.")
    text = st.text_area("Enter Passage")

    if st.button("Run Analysis"):
        with st.spinner("Processing..."):
            brief = generate_brief(text)
            st.markdown("### Summary Overview")
            st.write(brief)

            sentiment = infer_sentiment(text)
            st.markdown("### Dominant Emotion")
            st.write(sentiment)

            source = identify_source(text)
            st.markdown("### Probable Source")
            st.write(source)

            volume = compute_word_volume(text)
            st.markdown("### Word Count")
            st.write(volume)

if __name__ == "__main__":
    app()
