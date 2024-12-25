import os
import requests
from urllib.parse import urlparse
from pathlib import Path

def download_image(image_url: str, local_directory: str) -> str:
    Path(local_directory).mkdir(parents=True, exist_ok=True)
    response = requests.get(image_url)
    if response.status_code == 200:
        parsed_url = urlparse(image_url)
        image_name = os.path.basename(parsed_url.path)
        local_image_path = os.path.join(local_directory, image_name)
        with open(local_image_path, 'wb') as file:
            file.write(response.content)
        return local_image_path
    else:
        return "Failed to download image"