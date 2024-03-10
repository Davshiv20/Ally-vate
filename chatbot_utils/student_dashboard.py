import streamlit as st
import time
from student_dashboard_utils import Questionnaire, expected_answer, Rephrase,analyser
import chat_bot  # Assuming chat_bot doesn't import student_dashboard or exit directly

def initialize_chat_history():
    if "messages" not in st.session_state:
        st.session_state.messages = []

def display_chat_history():
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

def save_chat_history(filename="chat_history.txt"):
    if not st.session_state.messages:
        st.error("No messages to save. Chat history is empty.")
        return

    try:
        with open(filename, "w") as file:
            for message in st.session_state.messages:
                file.write(f"{message['role']}: {message['content']}\n")
        st.success("Chat history saved successfully!")
    except Exception as e:
        st.error(f"Error saving chat history: {e}")

def main():
    st.title("Ally-vate")
    st.subheader("Hello Student. This chat session was set in response to your low performance in Test.")
    st.markdown("We hope for your sincere contribution in this chatting session.\n:red[ Your responses will be used for further sessions.]")

    initialize_chat_history()
    display_chat_history()

    if "flag" not in st.session_state:
        st.session_state.flag = 1

    # Assistant asks questions
    if st.session_state.flag == 1:
            # Display assistant question in chat message container
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            
            # Get the question based on the current flag
            assistant_response = Questionnaire(st.session_state.flag)
            
            # Update the flag for the next user response
            st.session_state.flag += 1
            
            # Simulate stream of response with milliseconds delay
            for chunk in assistant_response.split():
                full_response += chunk + " "
                time.sleep(0.05)
                # Add a blinking cursor to simulate typing
                message_placeholder.markdown(full_response + "▌ ")
            message_placeholder.markdown(full_response)
       
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": full_response})


    # Student provides responses
    if prompt := st.chat_input("Student's Response"):
        st.session_state.flag-=1
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        updater=expected_answer(st.session_state.flag-1,prompt)
        if updater==1:
            st.session_state.flag+=1
        else:
            with st.chat_message("assistant"):
                message_placeholder=st.empty()
                full_response=""
                assistant_response=Rephrase()
                for chunk in assistant_response.split():
                    full_response += chunk + " "
                    time.sleep(0.05)
                    # Add a blinking cursor to simulate typing
                    message_placeholder.markdown(full_response + "▌ ")
                message_placeholder.markdown(full_response)
        
        if st.session_state.flag != 6:
            # Display assistant question in chat message container
            with st.chat_message("assistant"):
                message_placeholder = st.empty()
                full_response = ""
                
                # Get the question based on the current flag
                assistant_response = Questionnaire(st.session_state.flag)
                
                # Update the flag for the next user response
                st.session_state.flag += 1
                
                # Simulate stream of response with milliseconds delay
                for chunk in assistant_response.split():
                    full_response += chunk + " "
                    time.sleep(0.05)
                    # Add a blinking cursor to simulate typing
                    message_placeholder.markdown(full_response + "▌ ")
                message_placeholder.markdown(full_response)
                
            st.session_state.messages.append({"role": "assistant", "content": full_response})
    if st.session_state.flag==6:
        save_chat_history()
        with st.chat_message("assistant"):
                message_placeholder=st.empty()
                full_response=""
                assistant_response=analyser()
                for chunk in assistant_response:
                    full_response += chunk + ""
                    time.sleep(0.05)
                    # Add a blinking cursor to simulate typing
                    message_placeholder.markdown(full_response + "")
                message_placeholder.markdown(full_response)
                st.session_state.messages.append({"role": "assistant", "content": full_response})
                st.session_state.flag+=1
                
    # Final actions Consider integrating exit_page logic here or in a safe module without causing import loops
    if st.session_state.flag==7:
        exiting=st.button("Exit")
        if exiting:
            st.session_state["current_page"]="exit"
            exit.exit_page()
            
        if st.button("Ask Questions related to Acedemics and Career"):
                st.session_sstate["current_page"]="chat_bot"
                chat_bot.d_main()
                st.rerun()


# if __name__ == "__main__":
#     main()
