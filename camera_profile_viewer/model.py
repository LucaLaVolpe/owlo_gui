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

    def read_frame(self) -> np.ndarray:
        """Read frame."""
        index = int(time.time() * 10) % 100
        x, y = np.meshgrid(range(200), range(100))
        return (
            np.exp(-(x**2 + (y - 50) ** 2) / 400)
            + np.exp(-((x - 199) ** 2 + (y - 50) ** 2) / 400)
            + np.exp(-((x - 2 * index) ** 2 + (y - 50 + np.sin(index / 10) * 40) ** 2) / 1000)
        )

    def get_profiles(self, frame:np.ndarray) -> tuple[np.ndarray, np.ndarray]:
        """Return the profiles of the image along the x and y direction."""
        return frame.mean(axis=0), frame.mean(axis=1)

    def update_frame(self)->None:
        """Update the pyqt signal with the new frame."""
        if self.running:
            frame = self.read_frame()
            self.frame_updated.emit(frame)
