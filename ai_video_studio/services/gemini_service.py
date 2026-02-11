from __future__ import annotations

import asyncio
from dataclasses import dataclass

from ai_video_studio.config.settings import settings
from ai_video_studio.utils.retry import retry_async


@dataclass(slots=True)
class GeminiRequest:
    topic: str
    duration_seconds: int
    tone: str
    language: str
    platform: str


class GeminiService:
    async def generate_video_package(self, request: GeminiRequest) -> dict[str, object]:
        async def _call() -> dict[str, object]:
            await asyncio.sleep(0.2)
            return {
                "idea": f"{request.topic} breakdown for {request.platform}",
                "title": f"{request.topic} - Quick Guide",
                "description": "Auto-generated description.",
                "hashtags": ["#ai", "#automation", "#video"],
                "script": "Intro... Main idea... CTA.",
                "scenes": [{"prompt": "Scene 1 visuals", "duration_s": request.duration_seconds / 3}] * 3,
                "estimated_cost": 0.02,
            }

        return await asyncio.wait_for(retry_async(_call), timeout=settings.request_timeout_s)
