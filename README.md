#  YouTube Assistant  

A **Streamlit web app** to extract, summarize, translate, and interact with YouTube video transcripts using **Gemini AI**.  
*(Text-to-Voice feature coming soon!)*  



## Features  

- **Extract YouTube Transcripts**  
  - Enter any YouTube URL and fetch the transcript.  
  - Automatically grabs in the first available language.  
  - Handles long transcripts by chunking & summarizing in parts.  

- **Summarize Transcript**  
  - Get concise, **bullet-point summaries** powered by Gemini AI.  

- **View Transcript**  
  - Access the complete transcript in its original language directly from the sidebar.  

- **Ask Questions**  
  - Interactively ask about the video content.  
  - Receive **AI-powered answers** grounded in the transcript.  

- **Multilingual Support**  
  - Translate summaries and answers into **20+ languages** via Gemini.  
  - UI elements (buttons, headings, prompts) are instantly translated with `deep-translator`.  

- **Interactive UI**  
  - Clean Streamlit interface with **spinners, sidebars, and buttons** for smooth interaction.  

- **Text-to-Voice (Coming Soon)**  
  - Convert transcript summaries and answers into speech.  



##  Tech Stack  

- ``Streamlit``: For building the interactive web frontend.
- ``youtube-transcript-api``: To fetch YouTube video transcripts programmatically.
- ``google-generativeai (Gemini 2.0 Flash-Lite model)``: For summarization, translation, and question answering on video content. Model, rate, and token limits are configurable in `config.py`.
- ``deep-translator``: For translating UI elements content into multiple languages.
- ``python-dotenv``: Managing API keys securely.


##  Setup  

1. **Clone the repository:**
   ```bash
   git clone https://github.com/SaiSruthisri/YoutubeAssistant.git
   cd YoutubeAssistant
   ```

2. **Set up API keys:**
   - Create a `.env` file in the project root.
   - Add your Gemini API key:
     ```
     GEMINI_API_KEY=your_gemini_api_key_here
     ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app:**
   ```bash
   streamlit run app.py
   ```
   - After running, open your browser and go to [http://localhost:8501](http://localhost:8501) to use the app live.

##  Usage

1. **Choose Language:**  
   Select your preferred language for the UI and output.

2. **Enter YouTube URL:**  
   Paste a valid YouTube video URL in the input box.

3. **Load Transcript:**  
   Click "Load Transcript" to fetch and summarize the transcript.

4. **Summarize the Video:**  
   Click "📝Summarize the video" for a bullet-point summary.

5. **View Entire Transcript:**   
   After loading, you can view the complete transcript in its original language from the sidebar.

6. **Ask Questions:**  
   Type your question about the video and click "Ask" to get an AI-powered answer.

7. **Translate Transcript, Summary, and Answers:**  
   - Summaries and answers are generated in English by Gemini, then translated to your chosen language using Gemini for high quality.
   - UI elements (headings, buttons, prompts) are translated instantly using deep-translator for a native experience.

8. **Text to Voice:**  
   _Feature coming soon !_

> **Note:** Since this is a Streamlit app, always use the buttons in the intended order (e.g., Load Transcript → Summarize → Ask) to avoid losing data on the screen. Switching between buttons or reloading may reset the app state and clear your previous results or questions.


##  Supported Languages (for translation)

- English, Hindi, French, Spanish, German, Telugu, Kannada, Tamil, Russian, Portuguese, Italian, Dutch, Arabic, Korean, Turkish, Vietnamese, Filipino, Japanese, Chinese


##  Special Thanks & Documentation  

This project was made possible thanks to the following open-source libraries, documentation, and best practices:

- [Streamlit](https://streamlit.io/)
- [youtube-transcript-api](https://pypi.org/project/youtube-transcript-api/)
- [deep-translator](https://pypi.org/project/deep-translator/)
- [google-generativeai](https://pypi.org/project/google-generativeai/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- **Gemini API Rate Limiting:** Read about Gemini model rate limits and quotas [here](https://ai.google.dev/gemini-api/docs/rate-limits)
- **Retry Strategies:** Best practices for handling API retries and backoff are explained [here](https://cloud.google.com/storage/docs/retry-strategy#python)

##  Working flow


https://github.com/user-attachments/assets/ee644579-c555-4746-87f5-17a8467a0477

