import streamlit as st
import openai



# API Key 입력 받기
st.title("금태양 메이슨봇")
st.write("묻고 싶은게 있으면 대가를 내놔. 바보냐? 니 API키 말이야.")

# 키 저장
api_key = st.text_input("OpenAI API Key", type="password")
if api_key:
    st.session_state["api_key"] = api_key

# 전에 저장 한 키가 있으면 가져옴
if "api_key" in st.session_state:
    openai.api_key = st.session_state["api_key"]


question = st.text_input("오.. 입금 했냐 뭐가 궁금해서 나한테 오셨을까?")

@st.cache
def get_response_from_gpt(api_key, question):
    openai.api_key = api_key
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=question,
        max_tokens=100
    )
    return response.choices[0].text.strip()

# 질문이 있을 때 응답 받기
if question:
    if "api_key" in st.session_state:
        response = get_response_from_gpt(st.session_state["api_key"], question)
        st.write("GPT-3.5 Turbo로부터의 응답:")
        st.write(response)
    else:
        st.write("뭐하는 짓이냐? API키가 없잖아.")
