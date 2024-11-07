from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import openai
import requests
from core.openai_client import OpenAIClient  # Import OpenAI client

app = FastAPI()

class RequestModel(BaseModel):
    model: str
    prompt: str
    temperature: float = 0.7

@app.post("/generate_text")
async def generate_text(request: RequestModel):
    try:
        openai_client = OpenAIClient()  # Instantiate the OpenAI client
        response = await openai_client.generate_text(
            model=request.model,
            prompt=request.prompt,
            temperature=request.temperature,
        )
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)