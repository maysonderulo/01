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


#질문을 받아보
question = st.text_input("Enter your question")

@st.cache_data
def get_response_from_gpt(api_key, question):
    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "너는 정보를 제공해주는 유능한 챗봇이야."},
            {"role": "user", "content": question}
        ]
    )
    return response.choices[0].message['content']

# 질문이 있을 때 응답 받기
if question:
    if "api_key" in st.session_state:
        response = get_response_from_gpt(st.session_state["api_key"], question)
        st.write("Response from GPT-3.5 Turbo:")
        st.write(response)
    else:
        st.write("질문을 하고싶으시면 OpenAI API Key를 입력해주세요.")

