from gtts import gTTS
import os

def text_to_audio(text, filename="output.mp3", lang='en'):
    # Initialize gTTS with the text and language
    tts = gTTS(text=text, lang=lang, slow=False)
    
    # Save the audio file
    tts.save(filename)
    print(f"Success! Audio saved as {filename}")

if __name__ == "__main__":
    my_text = "Hello! I am your AI assistant, and I am converting this text to audio using the g-T-T-S library."
    text_to_audio(my_text)