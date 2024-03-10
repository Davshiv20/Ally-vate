from open_ai import call_openai_api

def main():
    # Another prompt for testing
    prompt = "Based on the recent performance of the student, provide personalized feedback to help them improve in their studies."

    # Call the OpenAI API with the new prompt
    try:
        response = call_openai_api(prompt)
        print("API Response:")
        print(response)
    except Exception as e:
        print("An error occurred while calling the OpenAI API:", e)

if __name__ == "__main__":
    main()
