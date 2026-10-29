# control the creativity and randomness of llm outputs
#temperature 
# top-k
# top-p
# and seed 
# thesea re the basically the knobs that shapes how the model generates text.

from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.environ["GEMINI_API_KEY2"]
client = genai.Client(api_key=API_KEY)


# Temperature
# Controls randomness. Higher = more creative/random. Lower = more focused/deterministic.

# 0.0 — Deterministic, always picks the most likely token
# 0.5 — Balanced
# 1.0 — Default, good balance
# 2.0 — Very creative, may be incoherent


# Top-p -> cumulative probability low top-p value more focused
# Token A: 40% → cumulative: 40%
# Token B: 30% → cumulative: 70%
# Token C: 15% → cumulative: 85%
# Token D: 10% → cumulative: 95%
# Token E:  5% → cumulative: 100%


# Top-p = 0.5 = fewer tokens = more focused

# Top-k
# Only consider the top k most likely tokens (by count, not probability).

# Example: Tokens ranked by probability:

# Token 1: 35%  ← Top 1
# Token 2: 25%  ← Top 2
# Token 3: 15%  ← Top 3
# Token 4: 10%  ← Top 4
# Token 5:  8%  ← Top 5
# Token 6:  4%
# Token 7:  2%
# ...
# Top-k 1 → Only Token 1 → Greedy (deterministic)
# Top-k 3 → Tokens 1, 2, 3 → Focused
# Top-k 40 → Top 40 tokens → Balanced (default)
# Top-k 100 → Top 100 tokens → More diverse
# Lower k = fewer tokens = more focused


def generate(prompt, temperature=1.0):
    response = client.models.generate_content(
        model='gemini-3.5-flash',
        contents = prompt,
        config= types.GenerateContentConfig(
            temperature=temperature
        )
    )
    return response.text


# temperature is the most important things. Start there , then finetune with top_p and top_k.



