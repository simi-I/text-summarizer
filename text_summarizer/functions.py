import openai
import streamlit as st

def create_prompt(text):
    prompt = f" Summarize this text:  {text}"
    return prompt
    

def summarize(prompt):
    try:
        response = openai.Completion.create(engine="gpt-3.5-turbo-instruct",
                                                prompt=create_prompt(prompt),
                                                max_tokens=512,  # we increased the tokens to get a longer blog post
                                                temperature=0.7)
        st.session_state["summary"] = response["choices"][0]["text"]
    except Exception as e:
        st.write('There was an error')
        st.write(e)
