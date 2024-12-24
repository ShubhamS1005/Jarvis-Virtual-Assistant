from openai import OpenAI
import os
api_key = os.getenv("OPENAI_API_KEY")

#pip install openai
client = OpenAI(
    api_key = os.getenv("OPENAI_API_KEY")
)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general task like    Alexa and Google Cloud."},
        {
            "role": "user",
            "content": "Write a haiku about recursion in programming."
        }
    ]
)

print(completion.choices[0].message)