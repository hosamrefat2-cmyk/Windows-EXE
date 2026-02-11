from __future__ import annotations

from PySide6.QtWidgets import QMainWindow, QTabWidget

from ai_video_studio.ui.dashboard import Dashboard
from ai_video_studio.ui.settings_panel import SettingsPanel
from ai_video_studio.ui.video_creator import VideoCreator


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("AI Video Automation Studio")
        self.resize(1100, 700)

        tabs = QTabWidget()
        tabs.addTab(Dashboard(), "Dashboard")
        tabs.addTab(VideoCreator(), "Create Video")
        tabs.addTab(SettingsPanel(), "Settings")
        self.setCentralWidget(tabs)
