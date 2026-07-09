import os
import json
from google import genai
from dotenv import load_dotenv

from .prompt import SYSTEM_PROMPT

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def process(records):
    prompt = f""" {SYSTEM_PROMPT}
 CSV Records:

 {json.dumps(records,indent=2)}

return only json
"""
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    text = response.text.strip()


   

    if text.startswith("```"):
        text = text.replace("```json", "").replace("```", "").strip()
    print("gemini Response")
    print(text)

    return json.loads(text)