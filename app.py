import streamlit as st 
import openai

st.title("GPT-3.5 Turbo Chatbot")
st.write("질문을 하고싶으시면 OpenAI API Key를 입력해주세요.")
#키를 입력받음
api_key = st.text_input("OpenAI API Key", type="password")
#키를 저장함
if api_key:
    st.session_state["api_key"] = api_key
#전에 키가 있으면 걍 불러옴
if "api_key" in st.session_state:
    openai.api_key = st.session_state["api_key"]



