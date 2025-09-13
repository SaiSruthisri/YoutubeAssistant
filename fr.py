from config import MODEL, RPM, TPM, RPD, CHARS_PER_TOKEN
from youtube_transcript_api import YouTubeTranscriptApi
from deep_translator import GoogleTranslator
from dotenv import load_dotenv
import streamlit as st
import google.genai as genai
import os, re, time, random

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

lang_choice = st.selectbox("🌍" + GoogleTranslator(source='en', target='en').translate("Choose Language:"), list(language_options.keys()))
target_lang = language_options[lang_choice]

def safe_generate(prompt,retries=3):
    retryable_errors = ("429", "408", "500", "502", "503", "504", "ResourceExhausted")
    for attempt in range(retries):
        try:
            rate_limit_pause()
            return client.models.generate_content(model=MODEL, contents=prompt)
        except Exception as e:
            if any(err in str(e) for err in retryable_errors):
                wait = (2 ** attempt) + random.uniform(0, 1) 
                time.sleep(wait)
            else:
                raise

def chunk_text(full_text,max_tokens=TPM//RPM):
    chunk_size = max_tokens*CHARS_PER_TOKEN
    return [full_text[i:i+chunk_size] for i in range(0, len(full_text), chunk_size)]

request_times = []
def rate_limit_pause():
    # time.sleep(60/RPM)
    now = time.time()
    while request_times and request_times[0] < now-60:
        request_times.pop(0)
    if len(request_times) >= RPM:
        sleep_for = 60 - (now - request_times[0])
        time.sleep(max(0, sleep_for)) 
    request_times.append(time.time())       

def ui_translate(text, target_lang):
    if target_lang == "en":
        return text
    try:
        return GoogleTranslator(source='en', target=target_lang).translate(text)
    except Exception:
        return text

def gemini_translate(text, target_lang):
    if target_lang == "en":
        return text
    resp = safe_generate(f"Translate the following text into {lang_choice} ({target_lang}):\n\n{text}")
    return resp.text.strip()


st.title(ui_translate("YouTube Assistant here", target_lang))
youtube_url = st.text_input(ui_translate("Enter your Youtube URL:", target_lang))
video_id=""
pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11})"
video_ID = re.search(pattern, youtube_url)  # Extract 1st videoID
if video_ID:
    video_id = video_ID.group(1)
    
## Load and summarize transcript
if st.button(ui_translate("Load Transcript", target_lang)):
    if video_id == "":
        st.error(ui_translate("Please enter a valid YouTube video URL!", target_lang))
    else:
        try:
            with st.spinner(ui_translate("Fetching and summarizing transcript...", target_lang)):
                ytt_api = YouTubeTranscriptApi()
                transcript_list = ytt_api.list(video_id)
                full_text = ""
                first_lang_transcript = next(iter(transcript_list))
                for item in first_lang_transcript.fetch():
                    full_text += item.text  
                st.session_state.transcript = full_text      

                chunks = chunk_text(full_text, max_tokens=TPM//RPM)
                summaries = []

                for chunk in chunks:
                    resp = safe_generate(
                        f"Summarize this transcript chunk concisely in English:\n\n{chunk}"
                    )
                    summaries.append(resp.text)

                master_summary_en = " ".join(summaries)
                master_summary = gemini_translate(master_summary_en, target_lang)
                st.session_state.summary = master_summary
                st.session_state.chat = [
                    {"role": "user", "parts": [f"Here is the summary of the transcript:\n\n{master_summary}"]}
                ]
                st.success(ui_translate("Transcript summarized! You can now ask questions below.", target_lang))

        except Exception as e:
            st.error(f"Error: {e}") 


st.write("What would you like to do next?")
col1, col2 = st.columns([1,1], gap="small") 
with col1:
    summarize_clicked = st.button("📝 " + ui_translate("Summarize the video", target_lang), key="summarize_btn" , type = "secondary")
with col2:
    transcript_clicked = st.button(ui_translate("View Entire Transcript(Original)", target_lang), key="full_transcript_btn", type = "tertiary")

if summarize_clicked:
    if not st.session_state.summary:
        st.error(ui_translate("Please load transcript first!", target_lang))
    else:
        with st.spinner(ui_translate("Summarizing video...", target_lang)):
            resp = safe_generate(
                f"Summarize the following transcript in nice bullet points in English. "
                f"Keep all important informative details in it:\n\n{st.session_state.transcript}"
            )
            final_summary_en = resp.text
            final_summary = gemini_translate(final_summary_en, target_lang)
            st.session_state.summary = final_summary
            st.write(final_summary)

if transcript_clicked:
    if not st.session_state.transcript:
        st.error(ui_translate("Please load transcript first!", target_lang))
    else:
        with st.spinner(ui_translate("Getting full transcript...", target_lang)):
            st.write(st.session_state.transcript)




user_question = st.text_input(ui_translate("Ask a question about the video:", target_lang))

if st.button(ui_translate("Ask", target_lang), type="primary"):
    if not user_question.strip():
        st.error(ui_translate("Please enter a question!", target_lang))
    elif not st.session_state.get("chat"):
        st.error(ui_translate("Load the transcript first!", target_lang))
    else:
        with st.spinner(ui_translate("Generating answer...", target_lang)):
            resp = safe_generate(f"""
            You are a helpful and friendly assistant & conversationalist. The user has provided a transcript summary of a YouTube video. 
            Your job is to answer their question in English in a clear, descriptive, and respectful way yet very friendly manner.  

            Guidelines:
            - Be conversational and approachable, but keep a polite and slightly obedient tone.  
            - Do not start answers with “The video says…” or similar. Instead, directly explain the content.  
            - Give maximum useful information from the transcript relevant to the user’s question.  
            - Organize explanations with clarity (use short paragraphs or bullet points if needed).  
            - If examples, timestamps, or details are mentioned in the video, include them naturally in your answer.  
            - Always stay accurate and avoid adding outside assumptions.  

            Transcript Summary:\n\n{st.session_state.summary}\n\nQuestion: {user_question}
            """)
            answer_en = resp.text
            answer = gemini_translate(answer_en, target_lang)
            st.session_state.chat.append({"role": "assistant", "content": answer })
            st.markdown(f"**{ui_translate('Answer:', target_lang)}** {answer}")
