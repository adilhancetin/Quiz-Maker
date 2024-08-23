import openai
import os

client = openai.OpenAI(
    api_key = os.getenv("api_key")
)

prompt = """
Give me 10 questions about the history of taekwondo in the following format:
1) <question>
a) <option-1>
b) <option-2>
c) <option-3>
d) <option-4>
2) <question>
a) <option-1>
b) <option-2>
c) <option-3>
d) <option-4>
...
At the end, provide the correct answers in this format:
answers: abcdabcdab
"""

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ],
    model="gpt-4o",
)

quiz = chat_completion.choices[0].message.content
print(quiz)
