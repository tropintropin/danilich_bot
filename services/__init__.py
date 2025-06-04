"""
Service module.

Admin-related functionalities:

- `is_admin`: Checks if a user is an admin based on their user ID.
"""

from .admins import is_admin

__all__ = [
    "is_admin",
]
