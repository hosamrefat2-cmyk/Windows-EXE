from __future__ import annotations

from pathlib import Path

from ai_video_studio.utils.helpers import ensure_dir


class ImageService:
    async def generate_scene_image(self, prompt: str, output_dir: str | Path, index: int) -> Path:
        out_dir = ensure_dir(output_dir)
        output = out_dir / f"scene_{index:02d}.txt"
        output.write_text(f"IMAGE PLACEHOLDER FOR: {prompt}", encoding="utf-8")
        return output
