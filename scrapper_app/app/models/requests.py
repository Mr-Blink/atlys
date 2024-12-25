from pydantic import BaseModel

class ScraperRequest(BaseModel):
    pages: int = 5
    url: str