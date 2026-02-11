from __future__ import annotations

from ai_video_studio.models.project_model import ProjectModel, ScenePlan
from ai_video_studio.services.gemini_service import GeminiRequest, GeminiService


class AIPipeline:
    def __init__(self, gemini_service: GeminiService | None = None) -> None:
        self.gemini_service = gemini_service or GeminiService()

    async def build_project(self, topic: str, duration_seconds: int, tone: str, language: str, platform: str) -> ProjectModel:
        payload = await self.gemini_service.generate_video_package(
            GeminiRequest(
                topic=topic,
                duration_seconds=duration_seconds,
                tone=tone,
                language=language,
                platform=platform,
            )
        )
        scenes = [ScenePlan(prompt=s["prompt"], duration_s=float(s["duration_s"])) for s in payload["scenes"]]
        return ProjectModel(
            title=str(payload["title"]),
            description=str(payload["description"]),
            script=str(payload["script"]),
            scenes=scenes,
        )
