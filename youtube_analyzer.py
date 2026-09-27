import os
from textwrap import dedent

import streamlit as st
from dotenv import load_dotenv

from agno.agent import Agent
from agno.models.openai import OpenAIResponses
from agno.tools.youtube import YouTubeTools


# Load variables from .env when running locally
load_dotenv()


def get_openai_api_key():
    """
    Get the OpenAI API key from:
    1. Local environment / .env file
    2. Streamlit Community Cloud secrets
    """

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        try:
            api_key = st.secrets.get("OPENAI_API_KEY")
        except Exception:
            api_key = None

    if not api_key:
        raise ValueError(
            "OPENAI_API_KEY is not configured. "
            "Add it to your local .env file or Streamlit Cloud Secrets."
        )

    # Make the key available to Agno/OpenAI through the normal environment
    os.environ["OPENAI_API_KEY"] = api_key

    return api_key


def build_youtube_agent():
    # Make sure the API key is available before creating the model
    get_openai_api_key()

    return Agent(
        name="YouTube Agent",

        model=OpenAIResponses(id="gpt-5.2"),

        tools=[YouTubeTools()],

        instructions=dedent("""\
            You are an expert YouTube content analyst with a keen eye for detail! 🎓

            Follow these steps for comprehensive video analysis:

            1. Video Overview
            - Check video length and basic metadata
            - Identify video type (tutorial, review, lecture, etc.)
            - Note the content structure

            2. Timestamp Creation
            - Create precise, meaningful timestamps
            - Focus on major topic transitions
            - Highlight key moments and demonstrations
            - Format: [start_time, end_time, detailed_summary]

            3. Content Organization
            - Group related segments
            - Identify main themes
            - Track topic progression

            Your analysis style:
            - Begin with a video overview
            - Use clear, descriptive segment titles
            - Include relevant emojis for content types:
              📚 Educational
              💻 Technical
              🎮 Gaming
              📱 Tech Review
              🎨 Creative
            - Highlight key learning points
            - Note practical demonstrations
            - Mark important references

            Quality Guidelines:
            - Verify timestamp accuracy
            - Avoid timestamp hallucination
            - Ensure comprehensive coverage
            - Maintain consistent detail level
            - Focus on valuable content markers
        """),

        add_datetime_to_context=True,
        markdown=True,
    )