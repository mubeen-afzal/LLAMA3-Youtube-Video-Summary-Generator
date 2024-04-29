import ollama
import streamlit as st
from typing import Dict, List
from youtube_transcript_api import YouTubeTranscriptApi


def get_video_id(url: str) -> str:
    url_components = url.split("?v=")
    if len(url_components) == 1:
        return None
    
    return url_components[1].split("&list=")[0]

def extract_clean_text(transcript_data: List[Dict]) -> str:
    transcript_text = " ".join(item["text"] for item in transcript_data)
    transcript_text = transcript_text.replace("\n", " ").strip()

    return transcript_text

def main():
    st.title("YouTube Transcript Summarizer")

    url = st.text_input("Enter YouTube URL:")
    if st.button("Summarize"):
        video_id = get_video_id(url)
        
        if video_id is None:
            st.error("Invalid URL. Please enter a valid YouTube video URL.")
            return
        
        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id)
        except:
            st.error("Either transcription not found or language is not English.")
            return

        transcript_text = extract_clean_text(transcript)

        # Call Ollama for summarization
        st.write("Summarized Text:")
        with st.spinner("Summarizing..."):
            stream = ollama.chat(model='llama3', messages=[
                {
                    "role": "system",
                    "content": "Your task is to summarize this text into multiple bullet points."
                },
                {
                    'role': 'user',
                    'content': transcript_text,
                }
            ], stream=True)

            all_text = ''
            container = st.empty()

            for chunk in stream:
                all_text += chunk['message']['content']
                container.markdown(all_text)

if __name__ == "__main__":
    main()
