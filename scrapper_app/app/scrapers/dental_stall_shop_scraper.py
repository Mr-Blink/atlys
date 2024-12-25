import os
import requests
from bs4 import BeautifulSoup
from typing import List
from app.scrapers.base_scraper import BaseScraper
from app.utils.image_downloader import download_image
from app.config import MAX_RETRIES, RETRY_DELAY
import time

class DentalStallShopScraper(BaseScraper):
    
    def scrape(self, url: str, pages: int = 5) -> dict:
        products = []
        local_directory = "./downloaded_images"
        if not os.path.exists(local_directory):
            os.makedirs(local_directory)
        for page_num in range(1, pages + 1):
            page_url = f"{url}page/{page_num}/" if page_num > 1 else url
            headers = {'User-Agent': 'Mozilla/5.0'}
            proxies = {"http": self.proxy, "https": self.proxy} if self.proxy else None
            attempt = 0
            response = None
            while attempt < MAX_RETRIES:
                try:
                    response = requests.get(page_url, headers=headers, proxies=proxies)
                    if response.status_code == 200:
                        break
                    else:
                        print(f"Received unexpected status code {response.status_code}. Retrying...")
                except Exception as e:
                    print(f"Attempt {attempt + 1} failed: {str(e)}. Retrying in {RETRY_DELAY} seconds...")
                    time.sleep(RETRY_DELAY)
                attempt += 1
            if not response or response.status_code != 200:
                print(f"Failed to retrieve page {page_url} after {MAX_RETRIES} attempts. Skipping...")
                continue

            soup = BeautifulSoup(response.text, 'html.parser')
            product_list = soup.select("#mf-shop-content ul.products li")
            
            for item in product_list:
                # Scrape product title
                product_title_element = item.select_one(".woo-loop-product__title a")
                if product_title_element:
                    product_title = product_title_element.get_text(strip=True)
                else:
                    product_title = "No title found"
                # Scrape product price
                product_price_element = item.select_one(".woocommerce-Price-amount")
                if product_price_element:
                    product_price = product_price_element.get_text(strip=True)
                else:
                    product_price = "No price found"
                # Scrape product image
                product_image_element = item.select_one(".mf-product-thumbnail img")
                if product_image_element and (product_image_element.has_attr('data-lazy-src') or product_image_element.has_attr('src')):
                    product_image_url = product_image_element.get('data-lazy-src', product_image_element.get('src'))
                    local_image_path = download_image(product_image_url, local_directory)
                else:
                    local_image_path = "No image found"
                print(f"Appending details for {product_title}")
                products.append({
                    "product_title": product_title,
                    "product_price": product_price,
                    "path_to_image": local_image_path,
                })
        return {"count": len(products), "products": products}
