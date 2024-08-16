## Simple FastAPI for Q&A LLM System

To activate your virtual environment, run the following commands in your terminal (ideally from your VS Code PowerShell):

- For venv
```
    # create the virtual environmnet
    python -m venv .venv

    # activate the virtual environmnet

    # Windows
    source .venv/Scripts/activate

    # Linux
    source .venv/bin/activate
```

- For poetry
```
    # create the virtual environmnet
    pip install poetry
    poetry new your_desired_venv_name
    poetry init
    poetry shell
    poetry add your_dependency
```

- For conda (Windows)
```
    # Open command prompt and activate conda base enviroment
     - skip this step if your Command prompt opens in a base environment, indicated with `(base)` at the start of your command line

    # run this command for Anaconda
    "C:\ProgramData\Anaconda3\Scripts\activate.bat"

    # run this for Miniconda
    "C:\ProgramData\Miniconda3\Scripts\activate.bat"

    # If the above doesn't work, then you probably did User installation of Anaconda or Miniconda
     - Navigate to the specific path it was installed in, and copy the full path to `activate.bat` file, then run it in your terminal.

    # Now that your command line is in the base environment, create a new virtual environment
    conda create -n your_desired_venv_name python=3.9

    # activate the environment
    conda activate your_desired_venv_name

```

# To install all dependencies in your requirements.txt, run the following command in your terminal - Command Prompt:

```pip install -r requirements.txt```


# To run app.py, run the following command in your terminal:

`uvicorn app:app --host 127.0.0.1 --port 5000 --reload`

You can update the host and port number to any other values you choose

Request body for testing in Postman

```
    {
        "question": "which is bigger? 9.11 or 9.9?",
        "model": "llama-3.1-8b-instant",
        "temperature": 0.2
    }
```

## Project Info
- Set up the conda virtual environment
- Activate the conda virtual environment
- Create the requirements.txt file and add all the libraries that are dependencies for the project
- Install all dependencies in requirements.txt by running the command: pip install -r requirements.txt
- Create the .env file and add the Groq API key
- Build the simple.py app
- Implement the API (app.py) and expose the endpoint 


- groq is the library we use to access the Groq platform, which gives us access to top open-source models. It also gives us accelerated inference on those models so we don't have to load them locally when trying to get inference from them.
- python-dotenv is a python library used to load environment variables from .env

- Groq is a hardware platform for deploying LLMs that require significant computational power. It's used to accelerate the inference phase, which is when the model is used to generate predictions or outputs from new data.
- FastAPI is a modern web framework for building APIs with Python. It’s typically used to build RESTful APIs or web service that allows other applications or users to interact with LLMs by sending requests and receiving responses. Once a model is trained and deployed (on hardware like Groq), FastAPI can be used to create an API endpoint that users can interact with to get predictions from the model.
- Uvicorn is a lightning-fast ASGI (Asynchronous Server Gateway Interface) server typically used to run FastAPI apps, handling incoming HTTP requests and routing them to the appropriate endpoints in your FastAPI app.
- Example Scenario:
Imagine you have an LLM deployed on Groq hardware. You want to provide access to this model via a web API so that users can interact with it (e.g., submit text and get predictions). Here's how it would work:
    # Groq provides the compute resources or takes care of the computation involved in running your LLM model.
    # FastAPI provides the API interface for users to interact with your model.
    # Uvicorn is the server that runs your FastAPI app, handling incoming requests and responses efficiently.

- Example Usage: 
After defining your FastAPI app (say, main.py), you can run it with the command ```uvicorn main:app --reload```. Here, main:app refers to your FastAPI app object, and Uvicorn is responsible for serving it. The --reload flag is useful during development as it automatically reloads the server whenever you make changes to your code.

- In Testing the Code in VS Code:
    # Run app.py in your terminal using uvicorn
    # The local host and port become active and the API server starts listening to them for requests
    # Send a request to this host and port from Postman
