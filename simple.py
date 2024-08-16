"""Build a simple LLM application"""

import os
import groq
from dotenv import load_dotenv

load_dotenv() # Instantiate load_dotenv. It parses the .env file and then load all the variables found as environment variables

# Set GROQ_API_KEY = "your api key" in the .env file, then load it below
GROQ_API_KEY = os.environ.get("GROQ_API_KEY") # Points to .env file and load the value of the API Key
groq_client = groq.Groq(api_key = GROQ_API_KEY) # The API value is passed to the Grog instance. This Groq instance can then be used to generate a chat completion functions and generate responses based on our questions

# A pre-define instruction that goes in everytime we interact with the model. It's not given any memory yet
sys_prompt = """You are a helpful virtual assistant. \
    Your goal is to provide useful and relevant \
        responses to my request"""

# Select some of the models supported by Groq Platform
models = [
    "llama-3.1-405b-reasoning",
    "llama-3.1-70b-versatile",
    "llama-3.1-8b-instant",
    "mixtral-8x7b-32768"
]

# Create a function that can take in the arguments for the model and user query to be passed to the model. The keyword argument temperature (min 0 and max 2)
# helps in testing how well the model performs under each temperature. Temperature determines how probabilistic the model will be when generating the
# responses. The further from zero, the more creative the model will be and the higher the tendency for hallucinations. Higher values like 0.8 and above
# will make the output more random, while lower values like 0.2 or less will make it more focused and deterministic.
def generate(model, query, temperature=0):

    response = groq_client.chat.completions.create(
        model = model,
        messages = [
            {"role": "system", "content": sys_prompt},
            {"role": "user", "content": query},
        ],
        response_format = {"type": "text"}, # This can be commented out bcos the default response format for LLMs is text. This line because useful when we need to force a response formay to, say, JSON
        temperature = temperature
    )

    answer = response.choices[0].message.content # To access the actual content of the response

    return answer


if __name__ == "__main__":
    model = models[2]
    query = "which is bigger? 9.11 or 9.9?"
    result = generate(model, query, temperature=0.4)
    print(result)
