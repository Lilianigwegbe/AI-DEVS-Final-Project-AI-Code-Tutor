import streamlit as st
import os
from groq import Groq
import json
import random

# Page configuration
st.set_page_config(
    page_title="AI Code Tutor",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize Groq client
@st.cache_resource
def init_groq_client():
    api_key = st.secrets.get("GROQ_API_KEY") or os.getenv("GROQ_API_KEY")
    if not api_key:
        st.error("Please set your GROQ_API_KEY in Streamlit secrets or environment variables")
        st.stop()
    return Groq(api_key=api_key)

def get_groq_response(client, prompt, system_message="You are a helpful coding tutor."):
    try:
        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": prompt}
            ],
            model="llama3-8b-8192",
            temperature=0.3,
            max_tokens=1000
        )
        return response.choices[0].message.content
    except Exception as e:
        st.error(f"Error calling Groq API: {str(e)}")
        return None

def main():
    # Custom CSS
    st.markdown("""
    <style>
    .main-header {
        text-align: center;
        padding: 1rem 0;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .feature-card {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #667eea;
        margin: 1rem 0;
    }
    .quiz-option {
        background: #e9ecef;
        padding: 0.5rem;
        margin: 0.5rem 0;
        border-radius: 5px;
        cursor: pointer;
    }
    .quiz-option:hover {
        background: #dee2e6;
    }
    </style>
    """, unsafe_allow_html=True)

    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🤖 AI Code Tutor</h1>
        <p>Your AI-Powered Coding Learning Assistant</p>
        <p><em>Supporting SDG 4: Quality Education</em></p>
    </div>
    """, unsafe_allow_html=True)

    # Initialize Groq client
    client = init_groq_client()

    # Sidebar for feature selection
    st.sidebar.title("Learning Hub")
    feature = st.sidebar.selectbox(
        "Choose a learning tool:",
        [
            "Code Explainer",
            "Debugging Assistant", 
            "Mini Lessons",
            "Quiz Generator",
            "Career Guide"
        ]
    )

    # Main content area
    if feature == "Code Explainer":
        code_explainer(client)
    elif feature == "Debugging Assistant":
        debugging_assistant(client)
    elif feature == "Mini Lessons":
        mini_lessons(client)
    elif feature == "Quiz Generator":
        quiz_generator(client)
    elif feature == "Career Guide":
        career_guide(client)

def code_explainer(client):
    st.header("Code Explainer")
    st.write("Paste your code below and get a natural language explanation!")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("Your Code")
        code_input = st.text_area(
            "Paste your code here:",
            height=300,
            placeholder="def fibonacci(n):\n    if n <= 1:\n        return n\n    return fibonacci(n-1) + fibonacci(n-2)"
        )
        
        language = st.selectbox(
            "Programming Language:",
            ["Python", "JavaScript", "Java", "C++", "HTML/CSS", "SQL", "Other"]
        )
        
        explain_btn = st.button("Explain Code", type="primary")
    
    with col2:
        st.subheader("Explanation")
        if explain_btn and code_input:
            with st.spinner("Analyzing your code..."):
                prompt = f"""
                Explain this {language} code in simple terms:
                
                ```{language.lower()}
                {code_input}
                ```
                
                Please provide:
                1. What this code does (in plain English)
                2. How it works step by step
                3. Key concepts used
                4. Any potential improvements or issues
                """
                
                explanation = get_groq_response(
                    client, 
                    prompt,
                    "You are a patient coding tutor who explains code clearly to beginners."
                )
                
                if explanation:
                    st.markdown(f"<div class='feature-card'>{explanation}</div>", unsafe_allow_html=True)

def debugging_assistant(client):
    st.header("Debugging Assistant")
    st.write("Having trouble with your code? Let's fix it together!")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("Problematic Code")
        buggy_code = st.text_area(
            "Paste your buggy code:",
            height=250,
            placeholder="for i in range(10)\n    print(i)"
        )
        
        error_message = st.text_area(
            "Error message (if any):",
            height=100,
            placeholder="SyntaxError: invalid syntax"
        )
        
        language = st.selectbox(
            "Language:",
            ["Python", "JavaScript", "Java", "C++", "Other"],
            key="debug_lang"
        )
        
        debug_btn = st.button("🔧Debug Code", type="primary")
    
    with col2:
        st.subheader("Debug Analysis")
        if debug_btn and buggy_code:
            with st.spinner("Debugging your code..."):
                prompt = f"""
                Help debug this {language} code:
                
                Code:
                ```{language.lower()}
                {buggy_code}
                ```
                
                Error message: {error_message if error_message else "No error message provided"}
                
                Please provide:
                1. What's wrong with the code
                2. The corrected version
                3. Explanation of the fix
                4. Tips to avoid similar bugs
                """
                
                debug_response = get_groq_response(
                    client,
                    prompt,
                    "You are an expert debugging assistant who helps students learn from their mistakes."
                )
                
                if debug_response:
                    st.markdown(f"<div class='feature-card'>{debug_response}</div>", unsafe_allow_html=True)

def mini_lessons(client):
    st.header("📚 Mini Lessons")
    st.write("Quick, focused lessons on programming concepts!")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Choose Your Topic")
        
        topic_category = st.selectbox(
            "Category:",
            ["Python Basics", "Web Development", "Data Structures", "Git/Version Control", "Algorithms", "Custom Topic"]
        )
        
        if topic_category == "Custom Topic":
            custom_topic = st.text_input("Enter your topic:")
            topic = custom_topic
        else:
            predefined_topics = {
                "Python Basics": ["Variables", "Lists", "Functions", "Loops", "Dictionaries", "Classes"],
                "Web Development": ["HTML Basics", "CSS Styling", "JavaScript", "APIs", "Responsive Design"],
                "Data Structures": ["Arrays", "Linked Lists", "Stacks", "Queues", "Trees", "Hash Tables"],
                "Git/Version Control": ["Git Basics", "Branching", "Merging", "Pull Requests", "Collaboration"],
                "Algorithms": ["Sorting", "Searching", "Recursion", "Dynamic Programming", "Big O Notation"]
            }
            
            topic = st.selectbox("Specific Topic:", predefined_topics[topic_category])
        
        lesson_length = st.selectbox(
            "Lesson Length:",
            ["Quick (3 sentences)", "Medium (1 paragraph)", "Detailed (2-3 paragraphs)"]
        )
        
        learn_btn = st.button("Start Lesson", type="primary")
    
    with col2:
        st.subheader("Your Lesson")
        if learn_btn and topic:
            with st.spinner("Preparing your lesson..."):
                length_instruction = {
                    "Quick (3 sentences)": "Explain in exactly 3 clear sentences",
                    "Medium (1 paragraph)": "Explain in one detailed paragraph",
                    "Detailed (2-3 paragraphs)": "Provide a comprehensive explanation in 2-3 paragraphs"
                }
                
                prompt = f"""
                Teach me about: {topic}
                
                {length_instruction[lesson_length]}.
                
                Include:
                1. What it is
                2. Why it's important
                3. A simple example
                4. One quick tip for beginners
                """
                
                lesson = get_groq_response(
                    client,
                    prompt,
                    "You are an engaging programming teacher who makes complex concepts easy to understand."
                )
                
                if lesson:
                    st.markdown(f"<div class='feature-card'>{lesson}</div>", unsafe_allow_html=True)

def quiz_generator(client):
    st.header("Quiz Generator")
    st.write("Test your knowledge with AI-generated coding quizzes!")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("Quiz Settings")
        
        quiz_topic = st.selectbox(
            "Topic:",
            [
                "Python Basics", "JavaScript Fundamentals", "HTML/CSS",
                "Data Structures", "Algorithms", "Git", "General Programming"
            ]
        )
        
        difficulty = st.selectbox(
            "Difficulty:",
            ["Beginner", "Intermediate", "Advanced"]
        )
        
        quiz_type = st.selectbox(
            "Quiz Type:",
            ["Multiple Choice", "Code Output", "Fill in the Blank", "True/False"]
        )
        
        generate_btn = st.button("Generate Quiz", type="primary")
    
    with col2:
        st.subheader("Your Quiz")
        if generate_btn:
            with st.spinner("Generating quiz questions..."):
                prompt = f"""
                Generate a {quiz_type} quiz question about {quiz_topic} at {difficulty} level.
                
                Format:
                Question: [The question]
                
                Options (if multiple choice):
                A) [Option 1]
                B) [Option 2] 
                C) [Option 3]
                D) [Option 4]
                
                Correct Answer: [Answer with explanation]
                
                Learning Tip: [One helpful tip related to the concept]
                """
                
                quiz_content = get_groq_response(
                    client,
                    prompt,
                    "You are a quiz creator who makes challenging but fair questions for coding students."
                )
                
                if quiz_content:
                    st.markdown(f"<div class='feature-card'>{quiz_content}</div>", unsafe_allow_html=True)
                    
                    # Add a "Generate Another" button
                    if st.button("Generate Another Question"):
                        st.rerun()

def career_guide(client):
    st.header("💼 Career Guide")
    st.write("Get personalized advice for your coding career journey!")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("Tell Us About Yourself")
        
        experience_level = st.selectbox(
            "Experience Level:",
            ["Complete Beginner", "Some Programming Knowledge", "Junior Developer", "Career Switcher"]
        )
        
        interests = st.multiselect(
            "Areas of Interest:",
            [
                "Web Development", "Mobile Development", "Data Science", 
                "Machine Learning/AI", "Game Development", "Cybersecurity",
                "DevOps", "Backend Development", "Frontend Development"
            ]
        )
        
        career_goal = st.selectbox(
            "Primary Goal:",
            [
                "Get my first programming job",
                "Switch to a tech career",
                "Learn programming as a hobby",
                "Advance to senior developer",
                "Start freelancing",
                "Build my own startup"
            ]
        )
        
        time_commitment = st.selectbox(
            "Time Available for Learning:",
            ["1-2 hours/day", "3-4 hours/day", "5+ hours/day", "Weekends only"]
        )
        
        get_advice_btn = st.button("Get Career Advice", type="primary")
    
    with col2:
        st.subheader("Your Personalized Career Guide")
        if get_advice_btn:
            with st.spinner("Preparing your career roadmap..."):
                prompt = f"""
                Provide career guidance for someone with:
                - Experience Level: {experience_level}
                - Interests: {', '.join(interests) if interests else 'General programming'}
                - Goal: {career_goal}
                - Time Available: {time_commitment}
                
                Please provide:
                1. Recommended learning path (specific technologies/skills)
                2. Timeline estimate
                3. Best resources to get started
                4. Tips for building a portfolio
                5. How to find internships/jobs/communities
                6. Next immediate steps to take
                """
                
                career_advice = get_groq_response(
                    client,
                    prompt,
                    "You are an experienced software engineering mentor who gives practical, actionable career advice."
                )
                
                if career_advice:
                    st.markdown(f"<div class='feature-card'>{career_advice}</div>", unsafe_allow_html=True)

    # Additional resources section
    st.markdown("---")
    st.subheader("Quick Resources")
    
    resource_cols = st.columns(3)
    
    with resource_cols[0]:
        st.markdown("**🎓 Free Learning Platforms**")
        st.markdown("- [freeCodeCamp](https://www.freecodecamp.org/)")
        st.markdown("- [Codecademy](https://www.codecademy.com/)")
        st.markdown("- [Khan Academy](https://www.khanacademy.org/computing)")
        st.markdown("- [MDN Web Docs](https://developer.mozilla.org/)")
        st.markdown("- [W3Schools](https://www.w3schools.com/)")
        st.markdown("- [Python.org Tutorial](https://docs.python.org/3/tutorial/)")
    
    with resource_cols[1]:
        st.markdown("**👥 Communities**")
        st.markdown("- [Stack Overflow](https://stackoverflow.com/)")
        st.markdown("- [GitHub](https://github.com/)")
        st.markdown("- [Reddit Programming](https://www.reddit.com/r/programming/)")
        st.markdown("- [Dev.to](https://dev.to/)")
        st.markdown("- [Hashnode](https://hashnode.com/)")
        st.markdown("- [Discord Coding Servers](https://disboard.org/servers/tag/programming)")
    
    with resource_cols[2]:
        st.markdown("**💼 Job Boards**")
        st.markdown("- [LinkedIn Jobs](https://www.linkedin.com/jobs/)")
        st.markdown("- [Indeed](https://www.indeed.com/)")
        st.markdown("- [AngelList](https://angel.co/jobs)")
        st.markdown("- [Remote.co](https://remote.co/)")
        st.markdown("- [We Work Remotely](https://weworkremotely.com/)")
        st.markdown("- [Glassdoor](https://www.glassdoor.com/)")

# Footer
def show_footer():
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666; padding: 1rem;'>
        <p>🤖 AI Code Tutor</p>
        <p>Built with Streamlit and Groq AI</p>
        <p>© 2025 AI DEVS</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
    show_footer()