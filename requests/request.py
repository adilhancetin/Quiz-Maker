import openai
import os

client = openai.OpenAI(
    api_key = os.getenv("api_key")
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Give me 10 questions about history of Turkey, the format will be like: 1)<question> a)<> ... . At the end give then answers like answers:abcdabcdab",
        }
    ],
    model="gpt-4o",
)

quiz = chat_completion.choices[0].message.content
print(quiz)
