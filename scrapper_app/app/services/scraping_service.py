from app.services.storage_factory import StorageFactory
from app.services.notification_factory import NotificationFactory
from app.scrapers.scraping_factory import ScrapingFactory

class ScrapingService:
    def __init__(self):
        self.storage = StorageFactory.get_storage("json")
        self.notifier = NotificationFactory.get_notifier("console")

    def scrape(self, url: str, pages: int) -> dict:
        scraper = ScrapingFactory.get_scraper(url)
        result = scraper.scrape(url, pages)
        self.storage.save(result["products"])
        self.notifier.notify(f"Scraped {result['count']} products.")
        return {"count": result["count"]}