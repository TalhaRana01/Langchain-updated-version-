import os
from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain.agents import create_agent




def get_weather(city: str) -> str:
    """Get the weather for a city."""
    return f"The weather in {city} is sunny"


llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

agent = create_agent(
    model=llm,
    tools=[get_weather],
    system_prompt="You are a helpful assistant."
)

# Run the agent
response = agent.invoke({
    "messages": [
        {"role": "user", "content": "What is the weather in New York?"}
    ]
})

print(response["messages"][-1])
