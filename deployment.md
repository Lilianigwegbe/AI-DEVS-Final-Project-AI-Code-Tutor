## AI Code Tutor Deployment Guide

This guide provides step-by-step instructions for deploying your AI Code Tutor application using Streamlit Cloud.

## Requirements
- GitHub account
- Groq API account and API key
- Streamlit Cloud account (free)
- Git installed locally
- Python 3.8+ installed

## Prerequisites
### Step 1:  Update repository files
### Step 2: Push to GitHub
### Step 3: Deploy on Streamlit Cloud

- Go to [share.streamlit.io](https://share.streamlit.io)
- Sign in with GitHub
- Click **"New app"**
- Select your repository: `LilianigwegbeAI-DEVS-Final-Project-AI-Code-Tutor`
- Main file: `app.py`
- Click **"Deploy!"**

### Step 4: Add API Key

- In your app dashboard, click **"⚙️ Settings"**
- Go to **"Secrets"**
- Add:
```toml
GROQ_API_KEY = "your_groq_api_key_here"
```
- Click **"Save"**


The app will be live at: `https://your-app-name.streamlit.app`

**Auto-updates**: Any GitHub push automatically redeploys your app.

## Troubleshooting

- **"No module named 'groq'"**: Check `requirements.txt`
- **"API key not found"**: Verify secrets in Streamlit dashboard
- **App won't load**: Check Streamlit Cloud logs in your app dashboard

---

**AI Code Tutor is now live and helping students worldwide!**