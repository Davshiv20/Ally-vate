import streamlit as st
from open_ai import call_openai_api  # Assuming call_openai_api is defined in open_ai module

def exit_page():
    st.title("Session ended")
    st.markdown("Thank You!")
    st.balloons()
    analyser()

def analyser():
    prompt = "Based on the given chat between assistant and user find whether the user require further assistance by a mentor and give answer in yes or no only"
    
    # Read chat history from file
    chat_history_file = "C:\\Users\\Shivam Dave\\Desktop\\Student-Guidance\\chatbot_utils\\chat_history.txt"
    with open(chat_history_file, 'r') as file:
        content = file.read()
    
    prompt = content + "\t" + prompt
    
    # Call OpenAI API for analysis
    output = call_openai_api(prompt)
    
    # Display the output within Streamlit
    st.write(output)
    
    # Check if mentor needs to be assigned based on the output
    check_first_line(str(output), "No")

def check_first_line(paragraph, target_word):
    # Split the paragraph into lines
    lines = paragraph.split(',')
    
    # Check if the first line starts with the target word
    if target_word in lines:
        return False
    else:
        st.write(lines[0])
        st.write("Mentor assigned")

# Ensure the exit_page() function is only called when the script is executed directly
if __name__ == "__main__":
    exit_page()
