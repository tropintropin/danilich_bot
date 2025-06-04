import logging

from core import redis
from core.constants import RedisKeys

logger = logging.getLogger(__name__)


async def is_admin(user_id: int) -> bool:
    """
    Check if a user is an admin.

    Args:
        user_id (int): The ID of the user to check.

    Returns:
        bool: True if the user is an admin, False otherwise.
    """
    return await redis.sismember(RedisKeys.ADMINS, user_id)
