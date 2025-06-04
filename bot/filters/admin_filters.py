"""Filters for the admin panel."""

from aiogram.filters import BaseFilter
from aiogram.types import CallbackQuery, Message

from services import is_admin


class IsAdminFilter(BaseFilter):
    """
    Filter to check if the user is an admin.

    Returns True if the user is an admin, False otherwise.
    """

    async def __call__(self, obj: Message | CallbackQuery) -> bool:
        user_id = obj.from_user.id
        return await is_admin(user_id)
