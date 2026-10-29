from google import genai
from google.genai import types
import os
from dotenv import load_dotenv
import tiktoken

#load .env file from the aprent dirtectory
load_dotenv(r"C:\Code\gen-ai\.env")

API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)

# tokens are the curreencyt of ai 
#1 every word you send costs money(input_tokens)
#2. every word the ai genrate the cost (output_tokens)

# 3. diff model have input and output tokens

#4. One word ≠ One token
# "Explain" = 1 token
# "database" = 1 token... but uncommon words split into 2-3 tokens
# Punctuation, numbers, special characters all count

# F1 - F IS ONE TOKEN AND 1 IS ANOTHER TOKEN

#5. Context windows are limited
# every prompt you sends uses up your availabel "memory"
#long prompts = less space for conversation
#less space = worse context awareness = worse answers


prompt_1 = "Hi Name is Vibhor. what is your name?"

response_1 = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=prompt_1
)
print(f"Response: {response_1}")

print(f"Response text: {response_1.text}")
print(f"\n📊 TOTAL TOKEN COUNT: {response_1.usage_metadata.total_token_count}")
print(f"   Input tokens (prompt): {response_1.usage_metadata.prompt_token_count}")
print(f"   Output tokens (response): {response_1.usage_metadata.candidates_token_count}")
print(f"   Thought tokens (Thinking): {response_1.usage_metadata.thoughts_token_count}")




# example 2: bad prompt
# vague prompts leads to verbopse , unfosed outputs

prompt_2 = """Explain database in brief."""

response_2 = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=prompt_2
)

print(f"Response text: {response_2.text}")
print(f"\n📊 TOTAL TOKEN COUNT: {response_2.usage_metadata.total_token_count}")
print(f"   Input tokens (prompt): {response_2.usage_metadata.prompt_token_count}")
print(f"   Output tokens (response): {response_2.usage_metadata.candidates_token_count}")
print(f"   Thought tokens (Thinking): {response_2.usage_metadata.thoughts_token_count}")


#3. Efficient prompt
prompt_3 = """You are a helpful assistant for college students.
Your job is to explain technical concepts in simple language.
Use examples whenever possible.
Avoid jargon and technical terms.
Be friendly and encouraging.
Keep responses concise but complete.

Now, explain what a database is to a college student.
Include a real-world example.
Explain why databases are important.
Keep it under 5 sentences."""

response_3 = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=prompt_3
)

print(f"Response text: {response_3.text}")
print(f"\n📊 TOTAL TOKEN COUNT: {response_3.usage_metadata.total_token_count}")
print(f"   Input tokens (prompt): {response_3.usage_metadata.prompt_token_count}")
print(f"   Output tokens (response): {response_3.usage_metadata.candidates_token_count}")
print(f"   Thought tokens (Thinking): {response_3.usage_metadata.thoughts_token_count}")