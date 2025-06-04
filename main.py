"""The entry point for the bot."""

import asyncio
import logging
import logging.config
from pathlib import Path

import yaml

from bot.handlers import admin_handlers
from core import bot, dp, redis, settings
from core.constants import RedisKeys


def setup_logging(
    default_path: str = "logging.yaml", default_level: int = logging.INFO
) -> None:
    """Set up the logging configuration."""
    if Path(default_path).is_file():
        with open(default_path, "r") as f:
            config = yaml.safe_load(f)
            logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)
        logging.warning(
            f"⚠ WARNING: Logging config file {default_path} not found, using basicConfig"
        )


async def main() -> None:
    """The main function to run the bot."""
    logger.info("Bot is starting...")

    logger.info("Loading base admin to Redis...")
    base_admin = settings.admin_id
    if not base_admin:
        logger.error("Base Admin ID is not set in the configuration.")
    else:
        await redis.sadd(RedisKeys.ADMINS, base_admin)
    logger.info(f"Base Admin ID {base_admin} loaded into Redis.")

    # TODO: Add additional setup below

    logger.info("Setting up handlers...")
    dp.include_router(admin_handlers.router)
    logger.info("Handlers set up successfully.")

    logger.info("Checking for existing webhook...")
    await bot.delete_webhook(drop_pending_updates=True)
    logger.info("Webhook deleted, starting polling...")

    await dp.start_polling(bot)
    logger.info("Bot is running.")


if __name__ == "__main__":
    setup_logging()
    logger = logging.getLogger(__name__)
    logger.info("Logging is set up.")

    asyncio.run(main())
