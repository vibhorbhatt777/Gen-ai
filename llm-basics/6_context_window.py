# Context window 
# What is Context Window?
# Context Window = Maximum tokens in a single request (combine both input tokens and output tokens )


# input tokens + output tokens <= Context Window 

# If your input uses 100,000 tokens out of a 128,000-token window,
# you only have up to 28,000 tokens left for the model's generated response.

# Different models have different limits:

# Gemini 2.5 Flash: ~1 million tokens
# GPT-4: ~128K tokens
# Claude 4: ~200K tokens

# input - 
# All previous messages (enitre converstion history)
#current message
# system prompt and instructions
# past conversation history
# uploaded files and images 


# Example: Context window = 128,000 tokens
# Suppose:
# - Input tokens = 100,000
# - Output tokens generated = 28,000
# - Total = 128,000 tokens
# At this point, the context window is full. the context window is HIT

# What happens next?
# 1. If the answer is complete: The model finishes normally.
# 2. If the answer is incomplete: The model may stop mid-sentence because it has no context capacity left for additional output.
# 3. If you send another message: The application may need to shorten or summarize the previous conversation to make room, or it may return a context-length error.

from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

load_dotenv(r"C:\Code\gen-ai\.env")

API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)



#as conversation grow , token accumulate

messages = []
def chat(user_message):
    """Send message and track tokens"""
    messages.append(
        types.Content(role="user", parts=[types.Part(text=user_message)])
    )
messages = []

def chat(user_message):
    """Send message and track tokens"""
    messages.append(
        types.Content(role="user", parts=[types.Part(text=user_message)])
    )
    
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=messages
    )
    
    messages.append(
        types.Content(role="model", parts=[types.Part(text=response.text)])
    )
    
    # Show token usage
    total_tokens = response.usage_metadata.total_token_count
    print(f"🤖: {response.text}")
    print(f"📊 Total tokens used: {total_tokens} (includes ALL {len(messages)} messages)\n")
    
    return response.text

# Start conversation
print("👤: Hi! My name is Yash")
chat("Hi! My name is Yash")

print("👤: I'm 25 years old")
chat("I'm 25 years old")

print("👤: I love Python programming")
chat("I love Python programming")

print("👤: I work as a software engineer")
chat("I work as a software engineer")

print("👤: What's my name?")
chat("What's my name?")
