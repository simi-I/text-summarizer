import streamlit as st
import openai
import os
from text_summarizer.functions import summarize

try:
    st.title("Text Summarizer")

    openai.api_key = os.getenv('OPENAI_KEY')

    # initialize state varibale
    if "summary" not in st.session_state:
        st.session_state["summary"] = ""

    input_text = st.text_area(label='Enter full text:', value="", height=250)

    st.button(
        "submit",
        on_click = summarize,
        kwargs={"prompt": input_text},
        )

    output_text = st.text_area(label="Sumarized text:", value= st.session_state["summary"], height=250)
except:
    st.write("There was an error :(")