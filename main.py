import streamlit as st
from ai import load_LLM, prompt

llm = load_LLM()

st.set_page_config(page_title="Email Beautifier", page_icon=":robot")
st.header("Email Beautifier")

col1, col2 = st.columns(2)

## Set Up Header Section
with col1:
    st.markdown("This is a tool that helps you improve the quality of your written emails using AI. This platform was built using Streamlit, Python, ChatGPT, and a couple small libraries to make the magic happen.")
    st.markdown("If you have any questions about the implementation, please reach out to me on Twitter @shaunakturaga.")
with col2:
    st.image("https://media1.giphy.com/media/kjpKQ8wXVVocN5IIyK/giphy.gif?cid=ecf05e47uh7j01cwdtx479ag9h4yf3ifajkjxt5apgpu89jl&rid=giphy.gif&ct=g", width=300)

## Set Up Input Area

st.markdown("## Enter Your Email to Convert")
col1, col2 = st.columns(2)

with col1:
        option_tone = st.selectbox(
            'Which tone would you like your email to have?',
            ('Formal', 'Informal')
        )

with col2:
        option_dialect = st.selectbox(
            'Which English dialect would you like?',
            ('American English', 'British English')
        )

def get_text():
    input_text = st.text_area(label="Please enter your email content",placeholder="Please enter your email content", key="email_content")
    return input_text

email_content = get_text()

st.markdown("### Your Converted Email")

if email_content:
    prompt_with_email = prompt.format(tone=option_tone,dialect=option_dialect,email=email_content)
    formatted_email = llm(prompt_with_email)
    st.write(formatted_email)


