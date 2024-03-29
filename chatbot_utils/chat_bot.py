import streamlit as st
import random
import time
from open_ai import call_openai_api
# model_loader()
def d_main():
    st.title("Ally-vate")

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Accept user input
    if u_prompt := st.chat_input("How's it going?"):
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(u_prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": u_prompt})

        # system_prompt = "you are a personalised career guidance to students, you will chat with students regarding their academic performance and their future career aspects. Answer queries related to this field only and deny any other questions."
        # input_prompt = system_prompt + "\n" + str(u_prompt)

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            
            # Generate response using the combined prompt
            assistant_response = call_openai_api(prompt=u_prompt)

            # Simulate stream of response with milliseconds delay
            for chunk in assistant_response:
                full_response += chunk + ""
                time.sleep(0.05)
                # Add a blinking cursor to simulate typing
                message_placeholder.markdown(full_response + "")

            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": full_response})

    
   
                                            
d_main()