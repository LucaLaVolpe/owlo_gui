"""Module containing the model, how we get a frame and extract profiles."""

import time

import numpy as np
from PySide6.QtCore import QObject, Signal


class CameraModel(QObject):
    """Class implementing the camera model."""

    frame_updated = Signal(np.ndarray)

    def __init__(self) -> None:
        """Init."""
        super().__init__()
        self.running = False
        self.x_range = 200
        self.y_range = 100

    def read_frame(self) -> np.ndarray:
        """Read frame."""
        frame_rate = 10
        amplitude, period = 40, 10
        sigma_1, sigma_2 = 400, 1000
        index = int(time.time() * frame_rate) % 100
        x, y = np.meshgrid(range(self.x_range), range(self.y_range))
        return (
            np.exp(-(x**2 + (y - self.y_range / 2) ** 2) / sigma_1)
            + np.exp(-((x - (self.x_range - 1)) ** 2 + (y - self.y_range / 2) ** 2) / sigma_1)
            + np.exp(
                -((x - 2 * index) ** 2 + (y - self.y_range / 2 + np.sin(index / period) * amplitude) ** 2) / sigma_2)
        )

    def get_profiles(self, frame: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
        """Return the profiles of the image along the x and y direction."""
        return frame.mean(axis=0), frame.mean(axis=1)

    def update_frame(self) -> None:
        """Update the pyqt signal with the new frame."""
        if self.running:
            frame = self.read_frame()
            self.frame_updated.emit(frame)
