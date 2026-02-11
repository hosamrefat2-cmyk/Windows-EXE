from __future__ import annotations

from datetime import datetime
from pathlib import Path


def timestamp_slug() -> str:
    return datetime.utcnow().strftime("%Y%m%d-%H%M%S")


def ensure_dir(path: str | Path) -> Path:
    target = Path(path)
    target.mkdir(parents=True, exist_ok=True)
    return target
