import os
import sys

# Make sure modify it so that Python runs the script with correct venv. (Wish there is a better way to hide it..)
sys.path.insert(0, r'C:\Users\wei19\OneDrive\01_CS_Python_Scripts_Backup\ChatWithAi\venv\Lib\site-packages')

from dotenv import load_dotenv
import openai

# Take environment variables from .env.
load_dotenv()

# Set up the OpenAI API client
openai.api_key = os.getenv('OPEN_API_KEY')

# Set up the model and prompt
model_engine = "text-davinci-003"


def run_chat():
    running_flag = True
    while running_flag:
        try:
            prompt = input("Type here:  ")

            # Generate a response
            completion = openai.Completion.create(
                engine=model_engine,
                prompt=prompt,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.5,
            )
            response = completion.choices[0].text
            print(f"OpenAI: {response}\n\n")
        except Exception as e:
            print(f"Exit with: {e}")
            running_flag = False


if __name__ == '__main__':
    run_chat()
    print("All done")
