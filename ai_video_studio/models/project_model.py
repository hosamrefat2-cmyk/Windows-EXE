from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path


@dataclass(slots=True)
class ScenePlan:
    prompt: str
    duration_s: float


@dataclass(slots=True)
class ProjectModel:
    title: str
    description: str
    script: str
    scenes: list[ScenePlan] = field(default_factory=list)
    voiceover_path: Path | None = None
    rendered_video_path: Path | None = None
