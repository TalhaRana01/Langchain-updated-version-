# import os 
# from dotenv import load_dotenv
# from langchain.chat_models import init_chat_model


# load_dotenv()


# # print(os.getenv("OPENAI_API_KEY"))
# # print(os.getenv("GOOGLE_API_KEY"))
# # print(os.getenv("GROQ_API_KEY"))
# # print(os.getenv("CLAUDE_API_KEY"))

# os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")


# models = init_chat_model("gpt-4o")

# # print(models)

# # invoke a model 

# response = models.invoke("Hello!, How are you?")

# print(response.content)


import os
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()

models = init_chat_model("google_genai:gemini-2.5-flash-lite")

# response = models.invoke("what is the capital of Pakistan?")
response = models.invoke("Hello, How are you?")

print(response.content)
# print(response.content)