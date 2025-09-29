import sys
from PySide6.QtWidgets import QApplication
from camera_profile_viewer.model import CameraModel
from camera_profile_viewer.view import CameraView

if __name__ == "__main__":
    app = QApplication(sys.argv)
    model = CameraModel()
    view = CameraView(model)
    view.show()
    sys.exit(app.exec())
