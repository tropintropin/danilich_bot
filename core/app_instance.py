"""
This module initializes the bot and dispatcher instances for the Telegram bot application.
It sets up the Redis storage for state management and configures the bot with the necessary properties.
"""

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.redis import RedisStorage
from redis.asyncio import Redis

from core import settings

redis: Redis = Redis(
    host=settings.redis_host,
    port=settings.redis_port,
    db=settings.redis_db,
    password=settings.redis_password,
)

redis_storage = RedisStorage(redis=redis)

bot = Bot(
    token=settings.bot_token,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML),
)

dp = Dispatcher(storage=redis_storage)
