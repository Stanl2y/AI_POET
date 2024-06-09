# from dotenv import load_dotenv
# load_dotenv() 이거말고 자동으로 api key를 가져오게 할 수 있음



from langchain_openai import ChatOpenAI
chat_model = ChatOpenAI()

# subject = "AI"
# result = chat_model.invoke(subject + "에 대한 시를 써줘.")
# print(result.content)

import streamlit as st
st.title("인공지능 시인")
subject = st.text_input("시의 주제를 입력해주세요")
st.write("시의 주제:" + subject)

if st.button("시를 작성"):
    result = chat_model.invoke(subject + "에 대한 시를 써줘")
    st.write(result.content)