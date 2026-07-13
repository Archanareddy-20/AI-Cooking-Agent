import os
from groq import Groq
from dotenv import load_dotenv
load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def head_chef_agent(dish):
    try:
        prompt = f"You are a professional Head Chef. Give a detailed step-by-step recipe for '{dish}'. Include ingredients and cooking steps."
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.1-8b-instant",
        )
        recipe = chat_completion.choices[0].message.content
        return f"👨‍🍳 **Head Chef**:\n{recipe}"
    except Exception as e:
        return f"👨‍🍳 **Head Chef Error**: {e}"
