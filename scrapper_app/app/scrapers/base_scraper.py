from abc import ABC, abstractmethod
from typing import Optional

class BaseScraper(ABC):

    def __init__(self, proxy: Optional[str] = None) -> None:
        super().__init__()
        self.proxy = proxy

    @abstractmethod
    def scrape(self, url: str, pages: int = 5) -> dict:
        pass