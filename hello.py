import streamlit as st
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown
import textwrap

GOOGLE_API_KEY='AIzaSyAuqov-2FATGUQoZeOoM88HScHWQT-hHlo'
genai.configure(api_key=GOOGLE_API_KEY)

st.title('🦜🔗 Quickstart App')

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

def generate_response(input_text):
    model = genai.GenerativeModel('gemini-pro')
    query_run = model.generate_content(input_text)
    return query_run

result = []
with st.form('my_form'):
    text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
    submitted = st.form_submit_button('Submit')
    response = generate_response(text)
    result.append(response.text)


st.info(result)
