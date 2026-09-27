from agno.agent import Agent
from agno.models.openai import OpenAIResponses
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools

from dotenv import load_dotenv

load_dotenv()

def build_agent():
    return Agent(
        model=OpenAIResponses(id="gpt-5.6-sol"),
        tools=[DuckDuckGoTools()],
        markdown=True,
        instructions="You are a helpful and expert travel agent.",
        add_datetime_to_context=True
    )

agent = build_agent()

agent.print_response("It is safe to travel to UAE today?")