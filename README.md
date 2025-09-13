# YouTube Assistant

A Streamlit web app to extract, summarize, translate, and interact with YouTube video transcripts using Gemini AI. (Text-to-Voice feature coming soon!)

## Tech Stack

- **Streamlit**: For building the interactive web frontend.
- **youtube-transcript-api**: To fetch YouTube video transcripts programmatically.
- **google-generativeai (Gemini 2.0 Flash-Lite model)**: For summarization, translation, and question answering on video content. Model, rate, and token limits are configurable in `config.py`.
- **deep-translator**: For translating UI elements content into multiple languages.
- **python-dotenv**: For secure management of API keys and environment variables.

## Features

- **Extract YouTube Transcripts:** Enter a YouTube URL and fetch the transcript (first available language).
- **Summarize Transcript:** Automatically summarizes the transcript using Gemini AI, with options for concise or bullet-point summaries.
- **Ask Questions:** Ask questions about the video content and get AI-powered answers based on the summary.
- **Interactive UI:** All features are accessible via a simple Streamlit interface.
**Translate Transcript, Summary, and Answers:** Translate summaries and answers to your chosen language using Gemini for high quality. UI elements are translated instantly using deep-translator.
- **Text to Voice:** _Coming soon !_

## Model & API Configuration

- The Gemini model and its limits (RPM, TPM, RPD, etc.) are set in `config.py`:
  - `MODEL`: Model name (default: `gemini-2.0-flash-lite-001`)
  - `RPM`: Requests per minute
  - `TPM`: Tokens per minute
  - `RPD`: Requests per day
  - `CHARS_PER_TOKEN`: Characters per token (for chunking)

## Setup

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
   streamlit run fr.py
   ```
   - After running, open your browser and go to [http://localhost:8501](http://localhost:8501) to use the app live.

## Usage

1. **Choose Language:**  
   Select your preferred language for the UI and output.

2. **Enter YouTube URL:**  
   Paste a valid YouTube video URL in the input box.

3. **Load Transcript:**  
   Click "Load Transcript" to fetch and summarize the transcript.

4. **Summarize the Video:**  
   Click "📝Summarize the video" for a bullet-point summary.

5. **View Entire Transcript:**
   After loading, you can view the complete transcript in the video's original language from the sidebar.

6. **Ask Questions:**  
   Type your question about the video and click "Ask" to get an AI-powered answer.

7. **Translate Transcript, Summary, and Answers:**  
   - Summaries and answers are generated in English by Gemini, then translated to your chosen language using Gemini for high quality.
   - UI elements (headings, buttons, prompts) are translated instantly using deep-translator for a native experience.

8. **Text to Voice:**  
   _Feature coming soon !_

## Supported Languages (for translation)

- English, Hindi, French, Spanish, German, Telugu, Kannada, Tamil, Russian, Portuguese, Italian, Dutch, Arabic, Korean, Turkish, Vietnamese, Filipino, Japanese, Chinese

## Notes

- The transcript is fetched in the first available language (usually English).
- Summarization and Q&A use Gemini AI (Google Generative AI) in English, then translate to the user's language if needed.
- UI elements are translated instantly using deep-translator.
- For long transcripts, the app automatically chunks and summarizes in parts.
- Model and API limits are configurable in `config.py`.
- **Important:** Since this is a Streamlit app, always use the buttons in the intended order (e.g., Load Transcript → Summarize → Ask) to avoid losing data on the screen. Switching between buttons or reloading may reset the app state and clear your previous results or questions.

## Troubleshooting

- **Transcript not found:** Some videos may not have transcripts available.
- **API errors:** Ensure your API key is valid and you have internet access.
- **Text too long:** The app automatically splits long transcripts for summarization.
- **Language not available:** If the requested transcript language (e.g., Telugu) is not available, the app will use the first available language.

## Special Thanks & Documentation

This project was made possible thanks to the following open-source libraries, documentation, and best practices:

- [Streamlit](https://streamlit.io/)
- [youtube-transcript-api](https://pypi.org/project/youtube-transcript-api/)
- [deep-translator](https://pypi.org/project/deep-translator/)
- [google-generativeai](https://pypi.org/project/google-generativeai/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- **Gemini API Rate Limiting:** Read about Gemini model rate limits and quotas [here](https://ai.google.dev/gemini-api/docs/rate-limits)
- **Retry Strategies:** Best practices for handling API retries and backoff are based on [Link](https://cloud.google.com/storage/docs/retry-strategy#python)

## License

MIT License
