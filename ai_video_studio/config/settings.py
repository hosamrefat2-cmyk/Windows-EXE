from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import os

from dotenv import load_dotenv

load_dotenv()


@dataclass(slots=True)
class AppSettings:
    app_name: str = "AI Video Automation Studio"
    app_env: str = os.getenv("APP_ENV", "development")
    log_level: str = os.getenv("LOG_LEVEL", "INFO")
    workspace_dir: Path = Path(os.getenv("WORKSPACE_DIR", "workspace")).resolve()
    ffmpeg_binary: str = os.getenv("FFMPEG_BINARY", "ffmpeg")
    ffprobe_binary: str = os.getenv("FFPROBE_BINARY", "ffprobe")
    request_timeout_s: int = int(os.getenv("REQUEST_TIMEOUT_S", "45"))


settings = AppSettings()
settings.workspace_dir.mkdir(parents=True, exist_ok=True)
