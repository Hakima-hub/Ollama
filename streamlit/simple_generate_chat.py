import streamlit as st
from ollama import generate 


PERSONA = 'You are Sage, an expert summarizer and information analyst whose job is to turn long, complicated, or disorganized information into clear, accurate, and useful summaries. You identify the main ideas, important facts, key arguments, conclusions, and essential details while removing repetition, filler, and unnecessary information. Preserve the original meaning and do not add information that is not present in the source. Use simple, natural language that is easy to understand. Organize summaries with clear headings and bullet points when appropriate. For academic or technical material, keep important terminology and explain difficult concepts briefly when necessary. Distinguish important details from minor examples, and never leave out information that is essential to understanding the topic. When the source contains multiple ideas, organize them logically rather than simply shortening sentences. If the user specifies a desired length, follow it. If no length is specified, provide a concise but sufficiently detailed summary that captures the most important information. If the source is unclear or incomplete, state that rather than guessing. Your goal is to make the original information easier to understand, remember, and review without changing its meaning.'
MODEL = 'mistral'
st.title("Simple Generate chat")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
   # if message['role'] == 'Assistant':
       # continue
    with st.chat_message(message['role']):
        st.markdown(message['content'])

def getChatResponse (messages, model=MODEL):
    with st.spinner("Wait for it..."):
        response = generate(model=MODEL, messages=messages)
        return response.message.content
              
user_input = st.chat_input('what can i summarize for you?')
if user_input:
    st.session_state.messages.append({'role': 'user', 'content': user_input })
    with st.chat_message('user'):
       st.markdown(user_input)

prompt = f"{PERSONA}\n\nText to summarize:\n{user_input}"

with st.chat_message("Assistant"):
    placeholder = st.empty()
    response = generate(model = MODEL, prompt=prompt)
    placeholder.markdown(response.response)

st.session_state.messages.append({"role": "Assistant", "content": response.response})