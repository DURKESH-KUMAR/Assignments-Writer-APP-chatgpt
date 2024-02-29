import streamlit as st
import openai

openai.api_key = "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"


def main():
    st.title("Assignments Writer APP!!")
    title = st.text_input("Whats your Title?")
    
    submit = st.button("write")
    if submit:
        messages = []
        system_msg = "chat bot"
        messages.append({"role": "system", "content": system_msg})
        
        
        message = title
        messages.append({"role": "user", "content": message})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages)
        reply = response["choices"][0]["message"]["content"]
        messages.append({"role": "assistant", "content": reply})
        st.write(reply)


if __name__ == '__main__':
    main()