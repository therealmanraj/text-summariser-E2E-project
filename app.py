from fastapi import FastAPI, Query
from fastapi.templating import Jinja2Templates
from fastapi.responses import Response
from starlette.responses import RedirectResponse
from textSummarizer.pipeline.prediction import PredictionPipeline
import uvicorn
import os

text: str = "What is text summarization for?"

app = FastAPI()

@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")

# Route to train the model
@app.get("/train", tags=["training"])
async def train():
    try:
        os.system("python main.py")
        return Response(content="Training completed successfully!", media_type="text/plain")
    except Exception as e:
        return Response(content=f"An error occurred: {e}", media_type="text/plain")

@app.get("/predict", tags=["prediction"])
async def predict(text):
    try:
        obj = PredictionPipeline()
        summary = obj.predict(text)
        return summary
    except Exception as e:
        return Response(content=f"An error occurred: {e}", media_type="text/plain")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
