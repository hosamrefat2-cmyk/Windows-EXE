from __future__ import annotations

from pathlib import Path

from ai_video_studio.utils.helpers import ensure_dir


class VoiceService:
    async def synthesize(self, text: str, output_dir: str | Path) -> Path:
        out_dir = ensure_dir(output_dir)
        output = out_dir / "voiceover.txt"
        output.write_text(f"VOICEOVER PLACEHOLDER\n{text}", encoding="utf-8")
        return output
