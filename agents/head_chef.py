import os
from groq import Groq

# Put your key here - no spaces
GROQ_API_KEY ="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"

client = Groq(api_key="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")

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