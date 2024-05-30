import streamlit as st
import openai


st.set_page_config(page_title="GPT-3.5 Turbo and DALL-E App", page_icon="🤖", layout="wide")

# Define a function to get the GPT-3.5 response
@st.cache_data
def get_gpt_response(api_key, question):
    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question}
        ]
    )
    return response.choices[0].message['content']

# Define a function to get the DALL-E image URL
@st.cache_data
def get_dalle_image(api_key, prompt):
    openai.api_key = api_key
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="512x512"
    )
    return response['data'][0]['url']

# Sidebar for navigation
page = st.sidebar.selectbox("Select a page", ["GPT-3.5 Chatbot", "DALL-E Image Generator"])

# Common API key input
api_key = st.sidebar.text_input("OpenAI API Key", type="password")
if api_key:
    st.session_state["api_key"] = api_key

# Page 1: GPT-3.5 Chatbot
if page == "GPT-3.5 Chatbot":
    st.title("금태양 메이슨봇")
    st.write("5252 묻고싶은게 있으면 API키를 내놔야할거 아냐?")
    
    question = st.text_input("뭐.. 그래서 묻고 싶은게 뭔데")
    
    if question:
        if "api_key" in st.session_state:
            response = get_gpt_response(st.session_state["api_key"], question)
            st.write("Response from GPT-3.5 Turbo:")
            st.write(response)
        else:
            st.write("야 장난하냐 API키 내놓으라고.")
    
# Page 2: DALL-E Image Generator
elif page == "DALL-E Image Generator":
    st.title("귀여운 고양이 달이의 그림판")
    st.write("안뇽뇽, 달이양 그림이 그리고 싶으면 API키와 프롬프트를 달라냥!")
    
    prompt = st.text_input("어떤 그림을 원하는지 설명해 달라냥")
    
    if prompt:
        if "api_key" in st.session_state:
            image_url = get_dalle_image(st.session_state["api_key"], prompt)
            st.image(image_url, caption="Generated by DALL-E", use_column_width=True)
        else:
            st.write("냥... API키를 적어주지 않으면 달이는 그림을 그릴수 없다냥...")
