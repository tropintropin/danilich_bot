"""Handlers for admin-related staff."""

import logging

from aiogram import Router
from filters import IsAdminFilter

router: Router = Router()
router.message.filter(IsAdminFilter())
router.callback_query.filter(IsAdminFilter())

logger = logging.getLogger(__name__)
logger.info("Admin handlers initialized.")
