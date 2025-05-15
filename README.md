# Multilingual-Audio-Processor

This project is a complete audio processing pipeline that converts speech from an MP3 file into translated spoken audio with background music. It leverages speech recognition, machine translation, speech synthesis, and audio editing techniques to create a smooth, multilingual audio experience.

🚀 Key Features
🔄 MP3 to WAV Conversion
Convert input MP3 files to WAV for compatibility with transcription tools.

📝 Speech Recognition
Transcribe audio using Google Speech Recognition.

🌍 Text Translation
Translate the transcribed text into any target language using deep_translator.

🔊 Text-to-Speech Synthesis
Convert the translated text into spoken audio using gTTS.

🎼 Background Music Mixing
Overlay the generated speech onto the original background music with fade-in/out effects.

🎚️ Vocal/Instrumental Separation
Separate vocals and accompaniment using Spleeter for cleaner audio mixing.

🧰 Requirements
Install all necessary packages via pip:

bash
Copy
Edit
pip install speechrecognition pydub gtts deep-translator spleeter
Also, make sure to install ffmpeg and have it available in your system PATH (used by pydub and spleeter).

📂 Project Structure
📁 your_project/
├── audio.py
├── TwinkleStar.mp3
├── TwinkleStar.wav
├── TwinkleStar_translated.mp3
├── TwinkleStar_final_output.mp3
└── separated_audio/
    └── TwinkleStar/
        ├── vocals.wav
        └── Accompaniment.wav
🧪 How It Works
Convert an input .mp3 file into .wav

Separate vocals and background music using Spleeter

Transcribe the speech from .wav

Translate the transcription to a target language (e.g., Telugu)

Generate speech from translated text

Merge the translated speech with the original background music

▶️ Run the Script
bash
python audio.py
Make sure to place your input MP3 file (e.g., TwinkleStar.mp3) in the same directory or update the path.

💡 Example Output
🎧 Input: TwinkleStar.mp3
📝 Transcribed Text: "Twinkle, twinkle, little star..."
🔁 Translated to Telugu: "ట్వింకిల్, ట్వింకిల్, లిటిల్ స్టార్..."
🎵 Final Output: TwinkleStar_final_output.mp3 (speech over music)
