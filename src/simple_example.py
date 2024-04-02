from autogen import AssistantAgent
import os
from groq import Groq


userData = {
    'GROQ_API_KEY': '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',
     "llm_name": "mixtral-8x7b-32768",
}


client = Groq(
    api_key=userData.get('GROQ_API_KEY'),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Explain the importance of low latency LLMs",
        },
    ],
    model=userData.get("llm_name"),
)

print(chat_completion)
