from pydantic import BaseModel, Field

class Note(BaseModel):
    title: str = Field(..., min_length=3)
    content: str = Field(..., min_length=5)
