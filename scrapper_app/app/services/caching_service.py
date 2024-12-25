import aioredis
from app.config import CACHE_TTL

class CacheService:
    def __init__(self):
        self.redis = aioredis.from_url("redis://localhost")

    async def set(self, key: str, value: str):
        await self.redis.set(key, value, ex=CACHE_TTL)

    async def get(self, key: str) -> str:
        return await self.redis.get(key)