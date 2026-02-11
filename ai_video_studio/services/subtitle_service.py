from __future__ import annotations

from pathlib import Path


class SubtitleService:
    async def generate_srt(self, script: str, output_path: str | Path) -> Path:
        output = Path(output_path)
        output.write_text("1\n00:00:00,000 --> 00:00:02,000\nAuto subtitle placeholder\n", encoding="utf-8")
        return output
