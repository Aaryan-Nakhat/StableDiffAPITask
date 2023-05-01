from fastapi import FastAPI, Request
import uvicorn
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from usermodels import UserPrompt
from textToSpeech import text2Speech, PATH


app = FastAPI()
prompt_passed = False
templates = Jinja2Templates(directory="templates")

@app.get("/")
def root():
    return f"Welcome Stable Diffusion API Users!"

@app.post("/predict")
async def predict(user_request: UserPrompt):
    global prompt_passed
    text_prompt = user_request.text_prompt
    prompt_passed = True
    return await text2Speech(text_prompt)


@app.get("/predict", response_class=HTMLResponse)
def get_predictions(request: Request):
    global prompt_passed
    if prompt_passed:
        return templates.TemplateResponse("index.html", {"request": request, "PATH": PATH})
    else:
        return "Pass in a text prompt first!"

if __name__ == "__main__":
    uvicorn.run(app=app, host="127.0.0.1", port=8000)
