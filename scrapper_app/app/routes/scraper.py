from fastapi import APIRouter, Depends, HTTPException, Header
from app.config import STATIC_TOKEN
from app.services.scraping_service import ScrapingService
from app.models.requests import ScraperRequest

scraper_router = APIRouter(prefix="/scraper", tags=["Scraper"])

def authenticate(authorization: str = Header(...)):
    if authorization != f"Bearer {STATIC_TOKEN}":
        raise HTTPException(status_code=401, detail="Invalid token")

@scraper_router.post("/start")
async def start_scraping(request: ScraperRequest, token: str = Depends(authenticate)):
    service = ScrapingService()
    result = service.scrape(request.url, request.pages)
    return {"message": f"Scraped {result['count']} products."}
