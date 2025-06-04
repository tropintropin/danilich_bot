from enum import StrEnum


class RedisKeys(StrEnum):
    """
    Redis keys used in the application.
    """

    ADMINS = "admins"
