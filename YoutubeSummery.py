from youtube_transcript_api import YouTubeTranscriptApi
import streamlit as st
from lama import process_large_transcript


st.set_page_config(page_title="Videonotes! 🎥", page_icon="📝", layout="centered")

# Custom CSS for the theme
st.markdown(
    """
    <style>
        /* Body styling */
        body {
            background-color: #ffffff;
            color:rgb(250, 0, 0);
            font-family: 'Arial', sans-serif;
        }
        /* Title styling */
        .css-1hvg8ba {
            color: #FFD700; /* Gold/Yellow title color */
        }
        
        /* Button styling */
        button {
            background-color: #FFD700;
            color: #000000;
            border-radius: 8px;
            border: none;
            font-size: 16px;
            padding: 8px 16px;
            cursor: pointer;
        }
        button:hover {
            background-color: #ffcc33;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Quickly Jot Down Notes for Your Video 📝")

# Description
st.write("Capture key points quickly to create engaging and impactful videos!")


url = st.text_input("Youtube Link", placeholder="Enter your Url...")



if(url):
    try:
        video_id=url.split("=")[1]
        try:
            transcripts = YouTubeTranscriptApi.list_transcripts(video_id)
            lang = ""
            for transcript in transcripts:
                lang = transcript.language_code
                break  

            Subs = YouTubeTranscriptApi.get_transcript(video_id, languages=[lang])
            try:
                with st.spinner('Processing...'):
                    result = process_large_transcript(Subs) 
                st.subheader("Generated Content:")
            except:
                st.info("Video is too long.")
            st.write(result)
        except:
            st.info("Sub Title Not Found")
    except :
        st.info("Give Correct URL")
        
