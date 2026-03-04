import os
import requests

from dotenv import load_dotenv
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise Exception("GROQ_API_KEY not set in environment variables")

def generate_answer(question: str, reference_text: str):
    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    prompt = f"""
You are a compliance assistant.

Answer the question ONLY using the provided reference documents.

If the answer is not found in the references, respond exactly:
Not found in references.

Answer in full sentence form.
Do not respond with only "Yes" or "No".

Return ONLY valid JSON.
Do not include explanations.
Do not include markdown formatting.
Do not wrap in triple backticks.
The response must be a raw JSON object.

Format:
{{
  "answer": "...",
  "citation": "exact sentence copied verbatim from the reference text"
}}

Reference Documents:
{reference_text}

Question:
{question}
"""

    payload = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0
    }

    response = requests.post(url, headers=headers, json=payload)
    result = response.json()

    print("GROQ RAW RESPONSE:", result)

    
    # added this because of groq rate limit
    #time.sleep method used to tackle this problem (takes a little more time)
    
    if "error" in result:
        if result["error"]["code"] == "rate_limit_exceeded":
            return """
    {
    "answer": "Generation delayed due to API rate limiting. Please retry.",
    "citation": ""
    }
    """
        raise Exception(f"Groq API Error: {result}")

    return result["choices"][0]["message"]["content"]