import time
import numpy as np
from PySide6.QtCore import QObject, Signal

class CameraModel(QObject):
    frame_updated = Signal(np.ndarray)

    def __init__(self):
        super().__init__()
        self.running = False

    def read_frame(self) -> np.ndarray:
        index = int(time.time() * 10) % 100
        x, y = np.meshgrid(range(200), range(100))
        out = (
            np.exp(-(x**2 + (y-50)**2)/400)
            + np.exp(-((x-199)**2 + (y-50)**2)/400)
            + np.exp(-((x-2*index)**2 + (y-50+np.sin(index/10)*40)**2)/1000)
        )
        return out

    def get_profiles(self, frame):
        return frame.mean(axis=0), frame.mean(axis=1)

    def update_frame(self):
        if self.running:
            frame = self.read_frame()
            self.frame_updated.emit(frame)
