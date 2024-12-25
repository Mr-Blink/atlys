from fastapi import FastAPI
from app.routes.scraper import scraper_router

app = FastAPI(title="Web Scraper API")

# Include routes
app.include_router(scraper_router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Web Scraper API"}
