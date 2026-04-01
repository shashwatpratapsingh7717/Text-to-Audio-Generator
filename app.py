import streamlit as st
from gtts import gTTS
import io

st.title("Text-to-Audio Converter")

# User Input
text_input = st.text_area("Enter your text here:", "Hello, welcome to my project!")
language = st.selectbox("Select Language", ["en", "es", "fr", "de", "hi"])

if st.button("Convert"):
    if text_input:
        # Generate speech in memory (using BytesIO) so we don't have to save a file
        tts = gTTS(text=text_input, lang=language)
        fp = io.BytesIO()
        tts.write_to_fp(fp)
        fp.seek(0)
        
        # Play in Streamlit
        st.audio(fp, format='audio/mp3')
    else:
        st.warning("Please enter some text.")