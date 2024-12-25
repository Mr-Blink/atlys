import json
from typing import List

class StorageInterface:
    def save(self, data: List[dict]):
        raise NotImplementedError

class JSONStorage(StorageInterface):
    def save(self, data: List[dict]):
        try:
            with open("scraped_data.json", "r") as f:
                existing_data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            existing_data = []
        existing_data.extend(data)
        with open("scraped_data.json", "w") as f:
            json.dump(existing_data, f, indent=4)
        print("Data appended to scraped_data.json")

class StorageFactory:
    @staticmethod
    def get_storage(storage_type: str) -> StorageInterface:
        if storage_type == "json":
            return JSONStorage()
        raise ValueError(f"Storage type '{storage_type}' not supported.")