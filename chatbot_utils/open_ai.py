# from openai import OpenAI
# import os

# def call_openai_api(prompt):
#     OPENAI_API_KEY = os.environ.get('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')
#     client = OpenAI(api_key=OPENAI_API_KEY)

#     chat_completion = client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role": "user", "content": f"{prompt}"},
#         ]
#     )

#     return chat_completion

from openai import OpenAI
# Replace 'your_api_key_here' with your actual OpenAI API key.
OPENAI_API_KEY = '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'

def call_openai_api(prompt):
    client = OpenAI(api_key=OPENAI_API_KEY)

    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"{prompt}"},
        ]
    )

    return chat_completion

# Usage
response = call_openai_api("Hello, world!")
print(response)

