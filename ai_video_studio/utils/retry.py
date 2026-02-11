from __future__ import annotations

import asyncio
from collections.abc import Awaitable, Callable
from typing import TypeVar

from ai_video_studio.utils.logger import get_logger

T = TypeVar("T")
logger = get_logger(__name__)


async def retry_async(
    func: Callable[[], Awaitable[T]],
    retries: int = 3,
    base_delay_s: float = 1.0,
) -> T:
    last_error: Exception | None = None
    for attempt in range(1, retries + 1):
        try:
            return await func()
        except Exception as exc:  # noqa: BLE001
            last_error = exc
            if attempt == retries:
                break
            delay = base_delay_s * (2 ** (attempt - 1))
            logger.warning("Attempt %s failed: %s. Retrying in %.1fs", attempt, exc, delay)
            await asyncio.sleep(delay)
    raise RuntimeError(f"Operation failed after {retries} attempts") from last_error
