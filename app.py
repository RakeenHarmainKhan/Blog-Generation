import streamlit as st 
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

# --- Styling ---
st.markdown("""
    <style>
        .main {
            background-color: #f5f7fa;
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0px 0px 8px rgba(0,0,0,0.1);
        }
        .title {
            font-size: 36px;
            color: #333;
            font-weight: 700;
            text-align: center;
            margin-bottom: 20px;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-size: 16px;
            border-radius: 10px;
            padding: 8px 16px;
            transition: background-color 0.3s ease;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- Function to get response from LLaMA 2 ---
def getLlamaResponse(input_text, no_words, blog_style):
    llm = CTransformers(model='D:\\Blog Generation\\models\\llama-2-7b-chat.ggmlv3.q8_0.bin',
                        model_type='llama',
                        config={'max_new_tokens': 256,
                                'temperature': 0.01})

    template = """
        Write a blog for {blog_style} job profile for a topic {input_text}
        within {no_words} words. 
    """

    prompt = PromptTemplate(input_variables=["blog_style", "input_text", 'no_words'],
                            template=template)

    response = llm(prompt.format(blog_style=blog_style, input_text=input_text, no_words=no_words))
    print(response)
    return response


# --- Page Config ---
st.set_page_config(page_title="Generate Blog",
                   page_icon="🌐",
                   layout="centered",
                   initial_sidebar_state="collapsed")

# --- Header ---
st.markdown("<div class='title'>🌐 AI Blog Generator</div>", unsafe_allow_html=True)

# --- Input Section ---
st.markdown("### ✍️ Enter your blog topic")
input_text = st.text_input("")

st.markdown("### 🧠 Choose style & word count")
col1, col2 = st.columns([5, 5])

with col1:
    no_words = st.text_input("Number of words")
with col2:
    blog_style = st.selectbox('Writing the blog for',
                              ('Researchers', 'Data Scientists', 'Common People'),
                              index=0)

# --- Submit Button ---
submit = st.button("🚀 Generate Blog")

# --- Output Section ---
if submit:
    if input_text.strip() == "" or no_words.strip() == "":
        st.warning("Please fill in all fields.")
    else:
        with st.spinner("Generating your blog... ✨"):
            blog = getLlamaResponse(input_text, no_words, blog_style)
            st.success("Done! 🎉")
            with st.expander("📃 View Generated Blog"):
                st.write(blog)

# --- Footer ---
st.markdown("""
<hr style="border:1px solid #ccc">
<p style='text-align: center; color: #999;'>Made using LLaMA 2 and Streamlit</p>
""", unsafe_allow_html=True)
