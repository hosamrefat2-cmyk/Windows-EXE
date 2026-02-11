from __future__ import annotations

from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget


class Dashboard(QWidget):
    def __init__(self) -> None:
        super().__init__()
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Dashboard"))
        layout.addWidget(QLabel("Track activity, usage, and recent renders."))
