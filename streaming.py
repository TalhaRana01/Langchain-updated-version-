from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")

# for chunk in model.stream("Write me a 200 words paragraph on Artificial Intelligence"):
for chunk in model.stream("Why do parrots have colorful feathers"):
  # print(chunk.text, end="|", flush=True)
  print(chunk.text, end="", flush=True)


# from langchain.agents import create_agent
# from langgraph.config import get_stream_writer  
# from dotenv import load_dotenv

# load_dotenv()

# # def get_weather(city: str) -> str:
# #     """Get weather for a given city."""
# #     writer = get_stream_writer()  
# #     # stream any arbitrary data
# #     writer(f"Looking up data for city: {city}")
# #     writer(f"Acquired data for city: {city}")
# #     return f"It's always sunny in {city}!"

# # agent = create_agent(
# #     model="gpt-4o-mini",
# #     tools=[get_weather],
# # )

# # for chunk in agent.stream(
# #     {"messages": [{"role": "user", "content": "What is the weather in SF?"}]},
# #     stream_mode="custom"
# # ):
# #     print(chunk)