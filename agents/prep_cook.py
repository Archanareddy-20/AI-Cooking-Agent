from groq import Groq

client = Groq(api_key="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")

def prep_cook_agent(dish):
    prompt = f"You are a Prep Cook. For the dish '{dish}', give a shopping list with quantities and total prep time."
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.1-8b-instant",
    )
    prep = chat_completion.choices[0].message.content
    return f"🥄 **Prep Cook**:\n{prep}"