from youtube_transcript_api import YouTubeTranscriptApi


video_id = "lWZ78Af53Xw"  
ytt_api = YouTubeTranscriptApi()
transcript_list = ytt_api.list(video_id)
transcript = ytt_api.fetch(video_id ,  languages=['te'])
translated_transcript = transcript.translate('en')
print(translated_transcript.fetch())

# print("This is a transcript list ------------")
# print(transcript_list)

# print("/////////////////////////////////////////////////////////////////////")

# print("This is the transcript ------------")
# print(transcript)



