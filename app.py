""" Build an API endpoint to access Simple App (through an http request over the web)
    This marks the entry point to the application.
    Once the app is started, app.py runs and execute uvicorn
    Once uvicorn is fired, the local host and port become active and the API server starts listening to them for requests
"""

from fastapi import FastAPI, Request
# from fastapi.responses import JSONResponse - Commenented out bcos we can now return an object from fastapi call. So, no need to Jsonify responses again; for instance, health() already returns an object
from simple import *  # * will import all the functions and variables in simple scripts

app = FastAPI()

# Ideally, it's good to have a healthcheker as the first thing in an API. Here, We define a health checker to determine that the API is running fine. At this point, we aren't passing any request to the app
@app.get('/healthz')
async def health():
    return {
        "application": "Simple LLM API",
        "message": "running succesfully"
    }

# We use a post request to pass request to the endpoint
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

# Start the app on the host and port specified, we can then make a call to it from postman
if __name__ == "__main__":
    import uvicorn
    print("Starting LLM API")
    uvicorn.run(app, host="0.0.0.0", reload=True)
