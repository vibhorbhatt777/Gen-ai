from google import genai
from google.genai import types
import os
from dotenv import load_dotenv
import gradio as gr 


load_dotenv(r"C:\Code\gen-ai\.env")

API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)
model_name = "gemini-3.5-flash-lite"

SYSTEM_INSTRUCTION = """
You are a senior AI tutor helping developers understand technical concepts.

Rules:
- Be concise but complete.
- Use simple, clear language.
- Avoid unnecessary fluff.
- Use short paragraphs.
- Provide examples when helpful.
- Do not assume prior deep knowledge unless asked.

Always prioritize clarity over complexity.
"""
MAX_CONTEXT_TOKENS = 25000 #simulated context window
INPUT_COST_PER_1K = 0.00035
OUTPUT_COST_PER_1K = 0.00053

#Memory Store 
chat_history = []

def send_message(user_input):
    global chat_history

    #*******append user_messages into chat_history**** - role - user
    chat_history.append(
        types.Content(
            role="user",
            parts=[types.Part(text=user_input)]
        )
    )
    
    #trim if needed
    trim_history()

    # generate response of the model by passing user prompt
    response = client.models.generate_content(
        model=model_name,
        contents=chat_history,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_INSTRUCTION
        )

    )

    reply= response.text # this is the llm model output when the llm give output
    
    #add llm model reply into chat_history
    chat_history.append(
        types.Content(
            role="model",
            parts=[types.Part(text=reply)]
        )
    )
    # now chat_history contain conatin both **user** as well as **llm model** in it.

    usage = response.usage_metadata

