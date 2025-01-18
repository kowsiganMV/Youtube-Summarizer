from youtube_transcript_api import YouTubeTranscriptApi
import streamlit as st
from lama import LLM

url = st.text_input("Youtube Link", "")


if(url):
    try:
        video_id=url.split("=")[1]
        transcripts = YouTubeTranscriptApi.list_transcripts(video_id)
        lang = ""
        for transcript in transcripts:
            lang = transcript.language_code
            break  

        Subs = YouTubeTranscriptApi.get_transcript(video_id, languages=[lang])
        with st.spinner('Processing...'):
            result = LLM(Subs) 
        st.subheader("Generated Content:")
        st.write(result.content)
    except :
        st.info("Subs Not found")
        