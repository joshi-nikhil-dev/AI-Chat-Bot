import sys
import asyncio
from tools.text_funifier import TextFunifier
from tools.text_summarizer import TextSummarizer
from tools.multiplication_tool import MultiplicationTool
from tools.vowel_counter import VowelCounter

class AIRoutingAgent:
    def __init__(self):
        """
        Initialize the AI Routing Agent with all the tools.
        """
        self.funifier = TextFunifier()  # DialoGPT for funifying
        self.summarizer = TextSummarizer()
        self.multiplication_tool = MultiplicationTool()
        self.vowel_counter = VowelCounter()

    async def route(self, user_input: str):
        """
        Route the user input to the appropriate tool based on the command.

        Supported Commands:
        - funify: Makes the input text funnier.
        - summarize: Summarizes the input text.
        - multiply: Multiplies a list of numbers.
        - count_vowels: Counts the number of vowels in the input text.

        Parameters:
        user_input (str): The prompt provided by the user.
        """
        if "funify:" in user_input.lower():
            text_to_funify = user_input.split("funify:")[1].strip()
            funified_text = self.funifier.funify(text_to_funify)
            print(f"Funified Text: {funified_text}")

        elif "summarize:" in user_input.lower():
            text_to_summarize = user_input.split("summarize:")[1].strip()
            summarized_text = self.summarizer.summarize(text_to_summarize)
            print(f"Summarized Text: {summarized_text}")

        elif "multiply:" in user_input.lower():
            numbers = self._extract_numbers(user_input)
            result = self.multiplication_tool.multiply_numbers(numbers)
            print(f"Product of {numbers}: {result}")

        elif "count_vowels:" in user_input.lower():
            text_to_count = user_input.split("count_vowels:")[1].strip()
            vowel_count = self.vowel_counter.count_vowels(text_to_count)
            print(f"Vowel Count in '{text_to_count}': {vowel_count}")

        else:
            print("Sorry, I didn't understand the request.")

    def _extract_numbers(self, text: str):
        """
        Helper function to extract numbers from a given text.
        
        Parameters:
        text (str): The input text containing numbers.
        
        Returns:
        List[int]: A list of extracted integers.
        """
        return [int(word) for word in text.split() if word.isdigit()]

async def main():
    agent = AIRoutingAgent()
    while True:
        user_prompt = input("Enter a prompt (or type 'exit' to quit): ")
        if user_prompt.lower() == "exit":
            print("Exiting...")
            break
        await agent.route(user_prompt)

if __name__ == "__main__":
    asyncio.run(main())  # Run the async main function
