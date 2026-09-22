import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SYSTEM_PROMPT = """
You are a general college assistant.

You do NOT have access to any private college database,
equipment records, student records, or booking information.

Answer using only your general language-model knowledge.

If a user asks about private college equipment availability,
student booking details, or private records, clearly state
that you do not have access to that private information.
"""

user_question = input("Ask the chatbot: ")

response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": user_question
        }
    ],
    temperature=0
)

print("\nPlain Chatbot:")
print(response.choices[0].message.content)