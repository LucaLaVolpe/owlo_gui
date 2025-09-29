"""View of the GUI."""

import numpy as np
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QPushButton, QVBoxLayout, QWidget

from camera_profile_viewer.model import CameraModel


class CameraView(QWidget):
    """Class to create the main window."""

    def __init__(self, model: CameraModel) -> None:
        """Init."""
        super().__init__()
        self.model = model

        # Button
        self.btn = QPushButton("Start")
        self.btn.clicked.connect(self.toggle)

        # Plots
        self.fig = Figure(figsize=(6, 6))
        self.canvas = FigureCanvas(self.fig)
        self.ax_img, self.ax_x, self.ax_y = (
            self.fig.add_subplot(311),
            self.fig.add_subplot(312),
            self.fig.add_subplot(313),
        )

        layout = QVBoxLayout()
        layout.addWidget(self.btn)
        layout.addWidget(self.canvas)
        self.setLayout(layout)

        # Timer for live updates
        self.timer = QTimer()
        self.timer.timeout.connect(self.refresh)

        # Connect model
        self.model.frame_updated.connect(self.update_plots)

    def toggle(self) -> None:
        """Toggle on off the start stop button."""
        self.model.running = not self.model.running
        self.btn.setText("Stop" if self.model.running else "Start")
        if self.model.running:
            self.timer.start(100)
        else:
            self.timer.stop()

    def refresh(self) -> None:
        """Update frame signal."""
        self.model.update_frame()

    def update_plots(self, frame:np.ndarray) -> None:
        """Update plots."""
        self.ax_img.clear()
        self.ax_img.imshow(frame)
        self.ax_img.set_title("Camera Frame")
        x_profile, y_profile = self.model.get_profiles(frame)
        self.ax_x.clear()
        self.ax_x.plot(x_profile)
        self.ax_x.set_title("X Profile")
        self.ax_y.clear()
        self.ax_y.plot(y_profile)
        self.ax_y.set_title("Y Profile")
        self.canvas.draw()
