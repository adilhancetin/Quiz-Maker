import openai
import os

def make_openai_request(topic):
    client = openai.OpenAI(
    api_key = os.getenv("api_key")
    )

    prompt = f"""
    Generate me 10 questions about the {topic} in the following format:
    0) <question>
    a) <option-1>
    b) <option-2>
    c) <option-3>
    d) <option-4>

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

    3) <question>
    a) <option-1>
    b) <option-2>
    c) <option-3>
    d) <option-4>

    4) <question>
    a) <option-1>
    b) <option-2>
    c) <option-3>
    d) <option-4>

    5) <question>
    a) <option-1>
    b) <option-2>
    c) <option-3>
    d) <option-4>

    6) <question>
    a) <option-1>
    b) <option-2>
    c) <option-3>
    d) <option-4>

    7) <question>
    a) <option-1>
    b) <option-2>
    c) <option-3>
    d) <option-4>

    8) <question>
    a) <option-1>
    b) <option-2>
    c) <option-3>
    d) <option-4>

    9) <question>
    a) <option-1>
    b) <option-2>
    c) <option-3>
    d) <option-4>

    answers:abcdabcdab
    ...
    Do not give anything besides this format. just questions and answer part in the given format. answer part is for example, all answers must be random. do not give explanation, comment or anything like that. And make sure that it is 10 questions.
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
    return quiz
