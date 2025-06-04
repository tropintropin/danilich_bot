"""
Core module for the application.

This module initializes and re-exports the main components of the application:

- `bot`: The main bot instance.
- `dp`: The dispatcher for handling updates.
- `redis`: The Redis client for caching and storage.
- `redis_storage`: The Redis storage for the dispatcher.
#
- `settings`: The configuration settings for the bot.

Example:
    from core import bot, dp, settings
"""

from .app_instance import bot, dp, redis, redis_storage
from .config import settings

__all__ = [
    "bot",
    "dp",
    "redis",
    "redis_storage",
    "settings",
]
