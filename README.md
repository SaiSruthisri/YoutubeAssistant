# YouTube Assistant

A Streamlit web app to extract, summarize, and interact with YouTube video transcripts using Gemini AI. (Translation and Text-to-Voice features coming soon!)

## Features

- **Extract YouTube Transcripts:** Enter a YouTube URL and fetch the transcript (first available language).
- **Summarize Transcript:** Automatically summarizes the transcript using Gemini AI, with options for concise or bullet-point summaries.
- **Ask Questions:** Ask questions about the video content and get AI-powered answers based on the summary.
- **Interactive UI:** All features are accessible via a simple Streamlit interface.
- **Translate Transcript:** _Coming soon!_
- **Text to Voice:** _Coming soon !_

## Special Thanks

This project was made possible thanks to the following open-source libraries and their documentation:

- [Streamlit](https://streamlit.io/)
- [youtube-transcript-api](https://pypi.org/project/youtube-transcript-api/)
- [deep-translator](https://pypi.org/project/deep-translator/)
- [google-generativeai](https://ai.google.dev/api/semantic-retrieval/question-answering#request-body)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

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

## Usage

1. **Enter YouTube URL:**  
   Paste a valid YouTube video URL in the input box.

2. **Load Transcript:**  
   Click "Load Transcript" to fetch and summarize the transcript.

3. **Summarize the Video:**  
   Click "Summarize the video" for a 100-word or bullet-point summary.

4. **Ask Questions:**  
   Type your question about the video and click "Ask" to get an AI-powered answer.

5. **Translate Transcript:**  
   _Feature coming soon !_

6. **Text to Voice:**  
   _Feature coming soon !_

## Supported Languages (for future translation)

- English, Hindi, French, Spanish, German, Telugu, Kannada, Tamil, Russian, Portuguese, Italian, Dutch, Arabic, Korean, Turkish, Vietnamese, Filipino, Japanese, Chinese

## Notes

- The transcript is fetched in the first available language (usually English).
- Summarization and Q&A use Gemini AI (Google Generative AI).
- For long transcripts, the app automatically chunks and summarizes in parts.

## Troubleshooting

- **Transcript not found:** Some videos may not have transcripts available.
- **API errors:** Ensure your API key is valid and you have internet access.
- **Text too long:** The app automatically splits long transcripts for summarization.

## License

MIT License
