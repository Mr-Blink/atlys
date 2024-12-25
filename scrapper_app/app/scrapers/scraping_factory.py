from app.scrapers.dental_stall_shop_scraper import DentalStallShopScraper
from app.scrapers.base_scraper import BaseScraper


class ScrapingFactory:
    scraper_map = {
        "https://dentalstall.com/shop/": DentalStallShopScraper,
    }
    
    @staticmethod
    def get_scraper(url: str) -> BaseScraper:
        if url in ScrapingFactory.scraper_map:
            return ScrapingFactory.scraper_map[url]()
        raise ValueError(f"No scraper found for URL: {url}")