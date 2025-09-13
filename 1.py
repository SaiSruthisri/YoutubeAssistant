# some changes to translate and get transcript

from youtube_transcript_api import YouTubeTranscriptApi
import streamlit as st
import google.genai as genai
from dotenv import load_dotenv
import os
import re 

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)


if "chat" not in st.session_state:
    st.session_state.chat = []
if "summary" not in st.session_state:
    st.session_state.summary = ""   
if "transcript" not in st.session_state:
    st.session_state.transcript = ""

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
lang_choice = st.selectbox("🌍 Choose Language:", list(language_options.keys()))
target_lang = language_options[lang_choice]

def translate_with_gemini(text, target_lang):
    """Translate any text using Gemini itself."""
    resp = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=f"Translate the following text into {lang_choice} ({target_lang}):\n\n{text}"
    )
    return resp.text.strip()

st.title("YouTube Assistant here")
youtube_url = st.text_input("Enter your Youtube URL:")
video_id=""
pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11})"
video_ID = re.search(pattern, youtube_url)  # Extract video ID from URL
if video_ID:
    video_id = video_ID.group(1)


## Load and summarize transcript
if st.button("Load Transcript"): 
    if video_id == "":
       st.error(translate_with_gemini("Please enter a valid YouTube video URL!", target_lang))
    else:
        try:
            ytt_api = YouTubeTranscriptApi()
            transcript_list = ytt_api.list(video_id)
            full_text = ""
            first_lang_transcript = next(iter(transcript_list))
            for item in first_lang_transcript.fetch():
                full_text += item.text  
            st.session_state.transcript = full_text      

            # Chunk transcript
            chunk_size = 3000    
            chunks = [full_text[i:i+chunk_size] for i in range(0, len(full_text), chunk_size)]

            summaries = []
            for chunk in chunks:
                resp = client.models.generate_content(
                    model="gemini-2.0-flash-001",   
                    contents=f"Summarize this transcript chunk concisely in {lang_choice} ({target_lang}):\n\n{chunk}"
                )
                summaries.append(resp.text)

            master_summary = " ".join(summaries)
            st.session_state.summary = master_summary
            st.session_state.chat = [
                {"role": "user", "parts": [f"Here is the summary of the transcript:\n\n{master_summary}"]}
            ]
            st.success(translate_with_gemini("Transcript summarized! You can now ask questions below.", target_lang))

        except Exception as e:
            st.error(f"Error: {e}") 


if st.button("Summarize the video"):
    if not st.session_state.summary:
        st.error(translate_with_gemini("Please load transcript first!", target_lang))
    else:
        resp = client.models.generate_content(
            model="gemini-2.0-flash-001",
            contents=f"""Summarize the following transcript in nice bullet points , keep all important informative details in it:
            Summarize the following transcript in {lang_choice} ({target_lang}) only.  (BUT )
    Rules:
    - Output must be purely in {lang_choice}, no English.
    - Use short bullet points .
    - Keep all important informative details.
            \n\n{st.session_state.transcript}"""
        )
        final_summary = resp.text
        st.session_state.summary = final_summary
        st.title(translate_with_gemini("📝 Short Summary of your Video", target_lang))
        st.write(final_summary , target_lang)

              

user_question = st.text_input(translate_with_gemini("Ask a question about the video:", target_lang))

if st.button("Ask", type="primary"):
    if not user_question.strip():
        st.error(translate_with_gemini("Please enter a question!", target_lang))
    elif not st.session_state.get("chat"):
        st.error(translate_with_gemini("Load the transcript first!", target_lang))
    else:
        resp = client.models.generate_content(
            model="gemini-2.0-flash-001",
            contents=f"""
            You are a helpful and friendly assistant. The user has provided a transcript summary of a YouTube video. 
Your job is to answer their question in {lang_choice} ({target_lang}) in a clear, descriptive, and respectful way.  

Guidelines:
- Be conversational and approachable, but keep a polite and slightly obedient tone.  
- Do not start answers with “The video says…” or similar. Instead, directly explain the content.  
- Give maximum useful information from the transcript relevant to the user’s question.  
- Organize explanations with clarity (use short paragraphs or bullet points if needed).  
- If examples, timestamps, or details are mentioned in the video, include them naturally in your answer.  
- Always stay accurate and avoid adding outside assumptions.  

Transcript Summary:\n\n{st.session_state.summary}\n\nQuestion: {user_question}"""
        )
        answer = resp.text
        st.session_state.chat.append({"role": "assistant", "content": answer })
        st.markdown(f"**{translate_with_gemini('Answer:', target_lang)}** {answer}")
