from __future__ import annotations

import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

from ai_video_studio.config.settings import settings


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger

    logger.setLevel(settings.log_level)
    logs_dir = Path(settings.workspace_dir) / "logs"
    logs_dir.mkdir(parents=True, exist_ok=True)

    formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    file_handler = RotatingFileHandler(logs_dir / "app.log", maxBytes=2_000_000, backupCount=3)
    file_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)
    logger.propagate = False
    return logger
