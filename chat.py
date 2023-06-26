import os
import sys

# If you'd like to run from short-cut or .bat, make sure to modify it so that Python runs the script with correct venv.
# Ignore this if you are running in interpreter such as PyCharm, simply set it in config.
# sys.path.insert(0, r'C:\Users\wei19\OneDrive\01_CS_Python_Scripts_Backup\ChatWithAi\venv\Lib\site-packages')

from dotenv import load_dotenv
import openai

# Take environment variables from .env.
load_dotenv()

# Set up the OpenAI API client
openai.api_key = os.getenv('OPEN_API_KEY')

# Set up the model and prompt
# https://platform.openai.com/docs/models/gpt-3
# model_engine = "text-davinci-003"
# model_engine = "text-davinci-002"
model_engine = "gpt-3.5-turbo"  # Endpoint: v1/chat/completions
# model_engine = "text-ada-001"  # very simple GPT-3, lowest cost


def run_chat():
    running_flag = True
    while running_flag:
        try:
            prompt = input("Type here:  ")

            # Generate a response
            if model_engine == "gpt-3.5-turbo":
                # as openai-0.27.8
                completion = openai.ChatCompletion.create(
                    model=model_engine,
                    messages=[{"role": "user", "content": prompt}]
                )
                response = completion['choices'][0].message.content
            else:
                # as openai-0.26.4
                completion = openai.Completion.create(
                    engine=model_engine,
                    prompt=prompt,
                    max_tokens=1024,
                    n=1,
                    stop=None,
                    temperature=0.5,  # randomness 0~2
                )
                response = completion.choices[0].text
            print(f"OpenAI:\n{response}\n--\n")
        except Exception as e:
            print(f"Exit with: {e}")
            running_flag = False


if __name__ == '__main__':
    run_chat()
    print("All done")
