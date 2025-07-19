import streamlit as st
import openai

# --- CONFIG ---
openai.api_key = st.secrets["OPENAI_API_KEY"]

# --- AUTO THEME DETECTION ---
st.set_page_config(page_title="AI Code Learning Assistant", layout="wide")

# JavaScript to detect user's preferred color scheme
auto_theme_js = """
<script>
    const darkMode = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
    window.parent.postMessage({isDark: darkMode}, '*');
</script>
"""
st.components.v1.html(auto_theme_js)

# Handle auto theme via Streamlit session state
def set_theme_if_not_set():
    if "dark_mode" not in st.session_state:
        st.session_state.dark_mode = False  # Default fallback

set_theme_if_not_set()

# Theme toggle with auto-detected preference listener
st.sidebar.title("🌓 Theme")
manual_toggle = st.sidebar.checkbox("Enable Dark Mode", value=st.session_state.dark_mode)
st.session_state.dark_mode = manual_toggle

custom_css = """
    <style>
    body {
        background-color: #0e1117;
        color: #FAFAFA;
    }
    .stTextInput > div > div > input, .stTextArea > div > textarea {
        background-color: #262730;
        color: #FAFAFA;
    }
    .stButton > button {
        background-color: #4CAF50;
        color: white;
    }
    </style>
"""

if st.session_state.dark_mode:
    st.markdown(custom_css, unsafe_allow_html=True)

# --- APP TITLE ---
st.title("AI Code Tutor")
st.markdown("Helping African learners unlock coding skills with AI ✨")

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("Features")
feature = st.sidebar.radio("Choose a feature:", [
    "Code Explainer",
    "Debugging Assistant",
    "Mini Lessons",
    "Quiz Generator",
    "Career Guide"
])

# --- HELPER FUNCTION ---
def ask_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful coding tutor."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

# --- CODE EXPLAINER ---
if feature == "Code Explainer":
    st.subheader("Explain Code")
    code = st.text_area("Paste your code here")
    if st.button("Explain") and code:
        with st.spinner("Explaining code..."):
            result = ask_gpt(f"Explain the following code in simple terms:\n{code}")
            st.success("Done!")
            st.markdown(result)

# --- DEBUGGING ASSISTANT ---
elif feature == "Debugging Assistant":
    st.subheader("Debug My Code")
    bug_code = st.text_area("Paste your buggy code")
    if st.button("Find and Fix Bugs") and bug_code:
        with st.spinner("Analyzing code for bugs..."):
            result = ask_gpt(f"Find and fix bugs in the following code:\n{bug_code}")
            st.success("Bugfix suggestions ready!")
            st.markdown(result)

# --- MINI LESSONS ---
elif feature == "Mini Lessons":
    st.subheader("On-Demand Mini Lessons")
    topic = st.text_input("Ask a coding topic (e.g., Python loops, Git basics)")
    if st.button("Teach Me") and topic:
        with st.spinner("Fetching lesson..."):
            result = ask_gpt(f"Give me a short lesson (3-5 sentences) on: {topic}")
            st.success("Here's your lesson")
            st.markdown(result)

# --- QUIZ GENERATOR ---
elif feature == "Quiz Generator":
    st.subheader("Generate a Quiz")
    quiz_topic = st.text_input("Enter a coding topic for a quiz")
    if st.button("Generate Quiz") and quiz_topic:
        with st.spinner("Creating quiz..."):
            result = ask_gpt(f"Create a short 3-question multiple choice quiz on: {quiz_topic}")
            st.success("Quiz ready!")
            st.markdown(result)

# --- CAREER GUIDE ---
elif feature == "Career Guide":
    st.subheader("Ask for Career Advice")
    career_question = st.text_input("Ask anything about your software career path")
    if st.button("Advise Me") and career_question:
        with st.spinner("Getting advice..."):
            result = ask_gpt(f"Give career advice: {career_question}")
            st.success("Here’s some advice:")
            st.markdown(result)

# --- FOOTER ---
st.markdown("---")
st.markdown("Empowering Next Generation of Developer in Africa🌍 | © 2025 CodeTutor")
