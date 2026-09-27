import streamlit as st

from youtube_analyzer import build_youtube_agent


st.set_page_config(
    page_title="YouTube Video Analyzer",
    layout="centered",
)


st.title("🎥 AI YouTube Video Analyzer")


@st.cache_resource
def get_agent():
    return build_youtube_agent()


video_url = st.text_input(
    "Enter YouTube Video Link",
    placeholder="https://www.youtube.com/watch?v=..."
)

button = st.button("Analyze Video")


if button:
    if not video_url.strip():
        st.warning("Please enter a YouTube video link.")
    else:
        try:
            with st.spinner("Analyzing video..."):
                agent = get_agent()

                response = agent.run(
                    f"Analyze this video: {video_url.strip()}"
                )

            st.markdown("### Analysis Report of Video:")

            if response and response.content:
                st.markdown(response.content)
            else:
                st.warning("No analysis was returned.")

        except Exception as error:
            st.error(f"Error: {error}")