"""The entry point for the bot."""

import asyncio
import logging
from pathlib import Path

import yaml


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
    pass


if __name__ == "__main__":
    setup_logging()
    logger = logging.getLogger(__name__)
    logger.info("Logging is set up.")

    pass
