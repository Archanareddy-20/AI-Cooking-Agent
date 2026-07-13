import os
import traceback  # add this
from dotenv import load_dotenv
from orchestrator import CookingWorkflow

load_dotenv()

def main():
    try:  # add this
        if not os.getenv("GROQ_API_KEY"):
            print("Error: Set GROQ_API_KEY in .env file")
            return

        print("Step 1: Creating workflow...")
        workflow = CookingWorkflow()
        print("Step 2: Workflow created!")

        print("4-Agent Cooking Project - Powered by Groq")
        dish = input("What do you want to cook? ")
        workflow.start_project(dish)

        while True:
            user_in = input("\nType DONE to continue cooking, REVIEW to get feedback, or QUIT: ").strip()
            if user_in.lower() == "quit":
                break
            elif user_in.lower() == "review":
                desc = input("Describe your final dish or upload issues: ")
                workflow.get_review(desc)
            else:
                workflow.next_step(user_in)
                
    except Exception as e:  # add this
        print("ERROR OCCURRED:")
        traceback.print_exc()

if __name__ == "__main__":
    main()