
# 💡 AI-DEVS-Final-Project-AI-Code-Tutor

**Live App**: [https://ai-code-tutor.streamlit.app/](https://ai-code-tutor.streamlit.app/)

Welcome to **AI Code Tutor**, an intelligent assistant designed to help learners improve their programming skills through personalized, real-time feedback and support. This project was developed as the final submission for the "AI in Software Engineering" course.

---

## 🚀 Project Overview

AI Code Tutor leverages machine learning and natural language processing to:
- Interpret and explain programming concepts.
- Offer real-time feedback on code.
- Guide learners through debugging.
- Suggest best practices and improvements.
- Support multiple programming languages and learning levels.

The application is built using **Streamlit** for the frontend interface and incorporates various AI/ML models for intelligent code assistance.

---

## 🧠 Key Features

- 🧪 **AI-Powered Code Analysis**  
  Understands user-submitted code and provides suggestions, explanations, and error insights.

- 💬 **Interactive Chat Interface**  
  Engages users in a conversational format to answer questions and guide learning.

- 🌐 **Streamlit Web App**  
  Simple, user-friendly UI for code input, feedback display, and interaction.

- 🛠️ **Modular Design**  
  Structured for easy updates, testing, and extension with more advanced models.

---

## 🗂️ Project Structure

```bash
├── .devcontainer/         # Development container configuration
├── .streamlit/            # Streamlit configuration files
├── Pitchdeck/             # Final project pitch presentation
├── Team/                  # Team contributions and documentation
├── app.py                 # Main application script
├── deployment.md          # Deployment instructions
├── requirements.txt       # Python dependencies
├── .gitignore             # Git ignored files
└── README.md              # Project documentation (you are here)

# 1. Clone the repository
git clone https://github.com/your-repo/ai-code-tutor.git
cd ai-code-tutor

# 2. (Optional) Create and activate a virtual environment
python -m venv venv
source venv/bin/activate           # On Linux/macOS
.\venv\Scripts\activate            # On Windows

# 3. Install required packages
pip install -r requirements.txt

# 4. Launch the Streamlit app
streamlit run app.py


