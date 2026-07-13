print("ORCHESTRATOR LOADING...")
import os
from langchain_community.chat_models import ChatGroq
from dotenv import load_dotenv
print("IMPORTS OK")

load_dotenv()

class CookingWorkflow:
    def __init__(self):
        print("INIT START")
        self.llm = ChatGroq(
            groq_api_key=os.getenv("GROQ_API_KEY"), 
            model_name="llama3-8b-8192", 
            temperature=0.7
        )
        print("INIT END - GROQ CONNECTED")
        self.step = 0
        self.dish = ""
        self.recipe = ""

    def start_project(self, dish):
        self.dish = dish
        print(f"\n=== RESEARCH CHEF ===")
        print(f"Finding the best recipe for {dish}...")
        self.recipe = self.llm.invoke(f"Give me a simple recipe for {self.dish} with ingredients and 5 steps").content
        print(self.recipe)
        print("\n--- Research Done ---")

    def next_step(self, user_input):
        self.step += 1
        print(f"\n=== HEAD CHEF ===")
        print(f"Moving to step {self.step} for {self.dish}")
        print("Type DONE when you finish this step")

    def get_review(self, description):
        print(f"\n=== FOOD CRITIC ===")
        print(f"Reviewing your {self.dish}...")
        review = self.llm.invoke(f"Review this dish based on: {description}. Give 2 tips to improve").content
        print(review)