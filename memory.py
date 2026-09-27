from agno.agent import Agent
from agno.models.groq import Groq
from agno.db.sqlite import SqliteDb
from rich.pretty import pprint

from dotenv import load_dotenv

load_dotenv()

db = SqliteDb(db_file="agno.db")
db.clear_memories()


def build_agent():
    return Agent(
        db=db,
        model=Groq(id="openai/gpt-oss-120b"),
        markdown=True,
        add_history_to_context=True,
        enable_agentic_memory=True
    )

agent = build_agent()

user_id = "rahul@gmail.com"
agent.print_response("I am Rahul & I am a Data Analyst.", user_id=user_id)
agent.print_response("who am I?", user_id=user_id)

memories = agent.get_user_memories(
    user_id=user_id
)

print("MEMORIES: ")
print(memories)

