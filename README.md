🎙️ Text-to-Audio Generator
A simple and fast Python script to convert raw text into natural-sounding audio using Google's Text-to-Speech (gTTS). No API keys or complicated setups required.

✨ Features
Zero Setup: Ready to use immediately without any authentication.

Multiple Languages: Supports English, Hindi, Spanish, and dozens of other languages.

Speed Control: Easily switch between normal and slow reading speeds.

Lightweight: Generates standard MP3 files with minimal system requirements.

🚀 Installation
1. Clone the repository:

Bash
git clone https://github.com/yourusername/text-to-audio-generator.git
cd text-to-audio-generator
2. Install the required library:

Bash
pip install gTTS
💻 Usage
Use the following Python code to generate your audio file.

Python
from gtts import gTTS

# 1. Enter your text
text_to_read = "Hello world! This is a simple text to audio generator."

# 2. Create the audio object
# Change lang='en' to 'hi' for Hindi, etc.
# Set slow=True if you want the audio to be slower.
tts = gTTS(text=text_to_read, lang='en', slow=False)

# 3. Save the file
tts.save("output.mp3")
print("✅ Audio successfully saved as output.mp3")
Reading from a File
If you want to read text from a .txt file instead:

Python
from gtts import gTTS

with open("script.txt", "r", encoding="utf-8") as file:
    text = file.read()

tts = gTTS(text=text, lang='en')
tts.save("audiobook.mp3")