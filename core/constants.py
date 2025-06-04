"""
Constants used in the application.

This module defines constants that are used throughout the application.
"""

from enum import StrEnum


class RedisKeys(StrEnum):
    """
    Redis keys used in the application.
    """

    ADMINS = "admins"
