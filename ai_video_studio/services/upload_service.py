from __future__ import annotations

from pathlib import Path


class UploadService:
    async def upload(self, platform: str, file_path: str | Path, title: str, description: str) -> dict[str, str]:
        return {
            "platform": platform,
            "status": "queued",
            "file": str(file_path),
            "title": title,
            "description": description,
        }
