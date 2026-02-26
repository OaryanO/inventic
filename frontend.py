import streamlit as st

from backend import generate_brief, infer_sentiment, identify_source, compute_word_volume

st.set_page_config(page_title="Inventic Assignment", page_icon="📚", layout="centered")
st.title("Inventic Assignment")
st.markdown("Analyze a literary excerpt and uncover meaningful insights.")

st.markdown("Provide a passage below and press 'Run Analysis' to view the results.")
text = st.text_area("Input your passage here:")

if st.button("Run Analysis"):
    with st.spinner("Processing the passage..."):

        volume = compute_word_volume(text)
        st.markdown("### Total Number of Words")
        st.write(volume)

        sentiment = infer_sentiment(text)
        st.markdown("### Predominant Emotion")
        st.write(sentiment)

        source = identify_source(text)
        st.markdown("### 2 - 3 Probable Books")
        st.write(source)

        brief = generate_brief(text)
        st.markdown("### Summary")
        st.write(brief)

        

        

