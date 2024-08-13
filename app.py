""" Build an API endpoint to access Simple App (through an http request over the web)
    This marks the entry point to the application.
    Once the app is started, app.py runs and execute uvicorn
    Once uvicorn is fired, the local host and port become active and the API server starts listening to them for requests
"""

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from simple import *

app = FastAPI()

@app.get('/healthz')
async def health():
    return {
        "application": "Simple LLM API",
        "message": "running succesfully"
    }


@app.post('/chat')
async def generate_chat(request: Request):

    query = await request.json()
    model = query["model"]
    
    try:
        temperature = float(query["temperature"])
    except:
        return {
            "error": "Invalid input, pass a number between 0 and 2."
        }

    if model not in models:
        return {
            "error": "You did not pass a correct model code!"
        }

    response = generate(
        model, 
        query["question"], 
        temperature=temperature
    )

    return {
        "status": "success",
        "response": response
    }


if __name__ == "__main__":
    import uvicorn
    print("Starting LLM API")
    uvicorn.run(app, host="0.0.0.0", reload=True)
