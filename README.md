# Jarvis - Voice Controlled Virtual Assistant 🗣️💻

Jarvis is a Python-based voice assistant that can perform various tasks like opening websites, playing songs, retrieving the latest news, and even generating AI responses using the OpenAI API.

## Features ✨

- Voice-activated trigger (`"Jarvis"`)
- Opens popular websites (Google, YouTube, Facebook, etc.)
- Plays pre-defined music tracks
- Fetches real-time news from Pakistan
- Uses OpenAI GPT-4o (via third-party endpoint) for intelligent conversation
- Text-to-speech responses using `pyttsx3`

## Requirements 📦

Install dependencies with:

```bash
pip install speechrecognition pyttsx3 requests openai

# For Windows:
pip install pipwin
pipwin install pyaudio

# For macOS/Linux:
brew install portaudio
pip install pyaudio

# Clone the repository:

```bash
git clone https://github.com/Emanijaz15/Virtual-AI-Assistant.git
cd jarvis-assistant

Add your API keys:

Replace "your api key here" in the search() function with your OpenAI key.

Replace the value of keyy with your NewsAPI key.

# Run the assistant:

```bash
python main.py
