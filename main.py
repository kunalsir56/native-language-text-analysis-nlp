import os
import time
import requests
import gradio as gr
from deep_translator import GoogleTranslator
from gtts import gTTS
import google.generativeai as genai

# ===============================
# ✅ CONFIGURATION (SECURE)
# ===============================

# Read API keys from environment variables
ASSEMBLYAI_KEY = os.getenv("ASSEMBLYAI_KEY")
GEMINI_KEY = os.getenv("GEMINI_KEY")

if not ASSEMBLYAI_KEY or not GEMINI_KEY:
    raise EnvironmentError("❌ API keys not found. Please set environment variables.")

os.environ["GOOGLE_API_KEY"] = GEMINI_KEY
genai.configure(api_key=GEMINI_KEY)

# Language name to code mapping
LANG_MAP = {
    "Hindi": "hi",
    "
