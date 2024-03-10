import streamlit as st
from student_dashboard_utils import model_loader
from .openai import call_openai_api
def exit_page():
    st.title("Session ended")
    st.markdown("Thank You!")
    st.balloons()
    analyser()
def analyser():
    model=model_loader()
    prompt="Based on the given chat between assistant and user find whether the user require furthur assistance by a mentor and give answer in yes or no only"
    global content
    with open("C:\\Users\\Shivam Dave\\Desktop\\Student-Guidance\\chatbot_utils\\chat_history.txt", 'r') as file:
        content = file.read()
    prompt=content+"\t"+prompt
    output=call_openai_api(prompt)
    print(output)
    
    check_first_line(str(output),"No")

def check_first_line(paragraph, target_word):
    # Split the paragraph into lines
    lines = paragraph.split(',')
    print(lines)
    # Check if the first line starts with the target word
    if target_word in lines:
        return False
    else:
        print(lines[0])
        print("Mentor assigned")
        # send_email("Student assingned ","Dear Mentor \n A student have been assigned to you for the mentorship session his session with the bot and his report card is attached along with this email. You can contact the student and decide the timings for the session accordingly.","9503adityas@gmail.com","/Users/adityasinha/Desktop/PROJECT/setmax/PythonFile/chat_history.txt")
        
exit_page()