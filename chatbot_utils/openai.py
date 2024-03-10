import openai
import os
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
def call_openai_api(prompt):
    openai.api_key = "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"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0125",
         messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"{prompt}"},
            # {"role": "assistant", "content": f"Answer: {answer}"},
            {"role": "user", "content": "Seeing to this is the student serious?"}
        ],
        
    )
    print(response)
    return response