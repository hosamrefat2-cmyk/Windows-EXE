from __future__ import annotations

from pathlib import Path

from ai_video_studio.models.project_model import ProjectModel
from ai_video_studio.services.image_service import ImageService
from ai_video_studio.services.video_service import VideoService
from ai_video_studio.services.voice_service import VoiceService


class RenderEngine:
    def __init__(
        self,
        image_service: ImageService | None = None,
        voice_service: VoiceService | None = None,
        video_service: VideoService | None = None,
    ) -> None:
        self.image_service = image_service or ImageService()
        self.voice_service = voice_service or VoiceService()
        self.video_service = video_service or VideoService()

    async def render(self, project: ProjectModel, output_dir: str | Path) -> ProjectModel:
        output_path = Path(output_dir)
        scene_assets = []
        for idx, scene in enumerate(project.scenes, start=1):
            scene_assets.append(await self.image_service.generate_scene_image(scene.prompt, output_path / "scenes", idx))

        project.voiceover_path = await self.voice_service.synthesize(project.script, output_path)
        project.rendered_video_path = await self.video_service.compose(scene_assets, project.voiceover_path, output_path)
        return project
