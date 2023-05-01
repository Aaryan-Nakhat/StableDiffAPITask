from pydantic import BaseModel

class UserPrompt(BaseModel):
    text_prompt: str