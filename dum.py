# test code to translate and get transcript
import streamlit as st
import re
from youtube_transcript_api import YouTubeTranscriptApi
from deep_translator import GoogleTranslator


st.title("Enter Youtube URL")
youtube_url = st.text_input("Enter your Youtube URL:")

video_id=""
pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11})"
video_ID = re.search(pattern, youtube_url)  # Extract video ID from URL
if video_ID:
    video_id = video_ID.group(1)

#First validate ID upon submit button
if st.button("Load Transcript"): 
    if video_id == "":
       st.error("Please enter a valid YouTube video URL!")
    else:
       st.success("Loaded your transcript ask your queries!")
# Language selection
language_options = {
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Telugu": "te",
    "Kannada": "kn",
    "Tamil": "ta",
    "Russian": "ru",
    "Portuguese": "pt",
    "Italian": "it",
    "Dutch": "nl",
    "Arabic": "ar",
    "Korean": "ko",
    "Turkish": "tr",
    "Vietnamese": "vi",
    "Filipino": "tl",
    "Japanese": "ja",
    "Chinese": "zh-CN"
}

if "translated_language" not in st.session_state:
    st.session_state["translated_language"] = "English"
    st.session_state["target_language_code"] = "en"

if st.button("Select Your Language", type="primary"):
    translated_language = st.selectbox("Select Language", list(language_options.keys()))
    st.session_state["translated_language"] = translated_language
    st.session_state["target_language_code"] = language_options[translated_language]

translated_language = st.session_state["translated_language"]
target_language_code = st.session_state["target_language_code"]

target_language_code="en"
if st.button("Get Transcript"):
    try:
        ytt_api = YouTubeTranscriptApi()
        transcript_list = ytt_api.list(video_id)
        full_text = ""
        first_lang_transcript = next(iter(transcript_list))
        for item in first_lang_transcript.fetch():
            full_text += item.text
        full_text = full_text.replace("'", "").replace('"', "")    

        if target_language_code != 'en':
            translator = GoogleTranslator(source='auto', target=target_language_code)
            translated_text = translator.translate(text=full_text)
            st.subheader(f"Translated Transcript ({translated_language}):")
            st.write(translated_text) 
        else:
            st.subheader("Original Transcript:")
            st.write(full_text)
    except Exception as e:
        if "No transcript found" in str(e):
            st.error("No transcript found for the provided YouTube URL.")
        elif video_id == "":
            st.error("Please enter a valid YouTube video URL!")