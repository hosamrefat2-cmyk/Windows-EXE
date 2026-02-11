from __future__ import annotations

from pathlib import Path

from ai_video_studio.utils.helpers import ensure_dir


class VideoService:
    async def compose(self, media_files: list[Path], voiceover: Path, output_dir: str | Path) -> Path:
        out_dir = ensure_dir(output_dir)
        output = out_dir / "rendered_video.txt"
        lines = ["VIDEO RENDER PLACEHOLDER", f"voiceover={voiceover}"] + [str(item) for item in media_files]
        output.write_text("\n".join(lines), encoding="utf-8")
        return output
