from __future__ import annotations

from dataclasses import dataclass
import os


@dataclass(slots=True)
class APIKeys:
    gemini_api_key: str = os.getenv("GEMINI_API_KEY", "")
    elevenlabs_api_key: str = os.getenv("ELEVENLABS_API_KEY", "")
    stability_api_key: str = os.getenv("STABILITY_API_KEY", "")
    youtube_client_id: str = os.getenv("YOUTUBE_CLIENT_ID", "")
    youtube_client_secret: str = os.getenv("YOUTUBE_CLIENT_SECRET", "")


api_keys = APIKeys()
