# AI Video Automation Studio (Windows EXE)

Production-oriented starter architecture for an AI-powered desktop app that generates and publishes social videos.

## Implemented in this phase

- Modular project scaffold following requested layers (`config`, `ui`, `services`, `engine`, `models`, `utils`).
- PySide6 desktop shell with tabs for Dashboard, Video Creation, and Settings.
- Async AI pipeline and render engine placeholders.
- Service interfaces for Gemini, voice, image, subtitle, video rendering, and upload.
- Logging, settings loading via `.env`, and async retry utility with exponential backoff.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m ai_video_studio.main
```

## Build EXE (planned)

```bash
pyinstaller --noconfirm --onefile --windowed ai_video_studio/main.py
```

## Next phases

1. Real API integrations (Gemini, ElevenLabs, image generation providers).
2. FFmpeg-based render composition (clips, transitions, subtitles, BGM).
3. OAuth publishing integrations (YouTube, TikTok, Facebook, Instagram).
4. Wizard workflows, progress/cancel, and autosave.
5. Production packaging, telemetry, hardening, and installer workflow.
