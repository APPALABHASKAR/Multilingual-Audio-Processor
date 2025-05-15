{
    # import whisper
# import speech_recognition as sr

# def transcribe_audio(audio_path):
#     # Load Whisper model
#     model = whisper.load_model("base")  # You can try "small" or "medium" for better accuracy

#     # Transcribe the file
#     result = model.transcribe(audio_path)

#     # Display results
#     print("✅ Detected Language:", result["language"])
#     print("📝 Transcription:\n", result["text"])

#     return result["language"], result["text"]

# # Test the recognizer
# r = sr.Recognizer()
# with sr.Microphone() as source:
#     print("Say something...")
#     audio = r.listen(source)
#     try:
#         text = r.recognize_google(audio)
#         print(f"You said: {text}")
#     except sr.UnknownValueError:
#         print("Could not understand audio")
#     except sr.RequestError as e:
#         print(f"Could not request results; {e}")

# # Run on your sample file
# if __name__ == "__main__":
#     transcribe_audio("TwinkleStar.mp3")
}

import speech_recognition as sr
from pydub import AudioSegment

def convert_mp3_to_wav(mp3_path, wav_path):
    sound = AudioSegment.from_mp3(mp3_path)
    sound.export(wav_path, format="wav")

def transcribe_audio_with_sr(audio_path):
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_path) as source:
        print("🎧 Listening to the audio...")
        audio_data = recognizer.record(source)

    try:
        print("📝 Transcribing...")
        text = recognizer.recognize_google(audio_data)
        print("✅ Transcription:\n", text)
        return text
    except sr.UnknownValueError:
        print("❌ Could not understand audio")
    except sr.RequestError as e:
        print(f"❌ Google Speech Recognition error: {e}")

from deep_translator import GoogleTranslator

def translate_text(text, target_language):
    try:
        translated = GoogleTranslator(source='auto', target=target_language).translate(text)
        print(f"🔁 Translated Text ({target_language}):\n{translated}")
        return translated
    except Exception as e:
        print(f"❌ Translation failed: {e}")
        return None

from gtts import gTTS

import os

def get_base_name(file_path):
    return os.path.splitext(os.path.basename(file_path))[0]


def text_to_speech(text, language_code, output_file):
    try:
        tts = gTTS(text=text, lang=language_code)
        tts.save(output_file)
        print(f"✅ Audio saved as {output_file}")
    except Exception as e:
        print(f"❌ Error: {e}")

# from pydub import AudioSegment

def merge_audio(speech_path, music_path, output_path, music_volume_reduction_db=10, fade_duration_ms=3000):
    # Load audio files
    speech = AudioSegment.from_file(speech_path)
    music = AudioSegment.from_file(music_path)

    # Adjust background music volume
    music = music - music_volume_reduction_db

    # Ensure music is at least as long as speech
    if len(music) < len(speech):
        # Loop the music to match the length of the speech
        loops = int(len(speech) / len(music)) + 1
        music = music * loops
    music = music[:len(speech)]

    # Apply fade-in and fade-out to the music
    music = music.fade_in(fade_duration_ms).fade_out(fade_duration_ms)

    # Overlay speech on background music
    combined = music.overlay(speech)

    # Export the final audio
    combined.export(output_path, format='mp3')
    print(f"✅ Merged audio saved as {output_path}")

from spleeter.separator import Separator

# def separate_audio(input_file, output_directory):
#     # Initialize Spleeter with 2 stems: vocals and accompaniment
#     separator = Separator('spleeter:2stems')

#     # Perform separation
#     separator.separate_to_file(input_file, output_directory)
#     print(f"✅ Separation complete. Files saved in {output_directory}")

def separate_audio(input_file, output_directory, custom_vocals_name=None, custom_accompaniment_name=None):
    # Initialize Spleeter
    separator = Separator('spleeter:2stems')
    separator.separate_to_file(input_file, output_directory)
    
    print(f"✅ Separation complete. Files saved in {output_directory}")

    # Get base name to locate output folder
    base_name = os.path.splitext(os.path.basename(input_file))[0]
    target_dir = os.path.join(output_directory, base_name)

    # Original Spleeter file names
    original_vocals = os.path.join(target_dir, "vocals.wav")
    original_accompaniment = os.path.join(target_dir, "accompaniment.wav")

    # Custom output names
    if custom_vocals_name:
        os.rename(original_vocals, os.path.join(target_dir, custom_vocals_name))
        print(f"🎙️ Vocals renamed to: {custom_vocals_name}")
    if custom_accompaniment_name:
        os.rename(original_accompaniment, os.path.join(target_dir, custom_accompaniment_name))
        print(f"🎶 Accompaniment renamed to: {custom_accompaniment_name}")



# Run it on TwinkleStar.mp3
if __name__ == "__main__":
    mp3_file = "TwinkleStar.mp3"
    base_name = get_base_name(mp3_file)
    wav_file = f"{base_name}.wav"
    convert_mp3_to_wav(mp3_file, wav_file)
    output_directory = f"separated_audio/{base_name}"
    os.makedirs(output_directory, exist_ok=True)
    separate_audio(mp3_file, output_directory,
               custom_vocals_name="vocals.wav",
               custom_accompaniment_name="Accompaniment.wav"
    )
    text_to_translate=transcribe_audio_with_sr(wav_file)
    translated_text=translate_text(text_to_translate, "te")
    output_audio_file = f"{base_name}_translated.mp3"
    text_to_speech(translated_text,'te',output_audio_file)
    music_path = f"separated_audio\{base_name}\{base_name}\Accompaniment.wav"
    final_output_file = f"{base_name}_final_output.mp3"
    merge_audio(output_audio_file, music_path, final_output_file)