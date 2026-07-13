from groq import Groq

client = Groq(api_key=("GROQ_API_KEY"))

def food_critic_agent(dish, recipe):
    try:
        prompt = f"You are a Food Critic. Review the dish '{dish}'. Recipe details: {recipe}. Give a rating out of 10 and 2 suggestions to improve taste."
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.1-8b-instant",
        )
        review = chat_completion.choices[0].message.content
        return f"🧑‍⚖️ **Food Critic**:\n{review}"
    except Exception as e:
        return f"🧑‍⚖️ **Food Critic Error**: {e}"
