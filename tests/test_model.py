"""Tests for the model."""
import numpy as np

from camera_profile_viewer.model import CameraModel


def test_read_frame_shape() -> None:
    """Test that read_frame returns a frame with shape 100, 200."""
    model = CameraModel()
    frame = model.read_frame()
    assert isinstance(frame, np.ndarray)
    assert frame.shape == (100, 200)

def test_get_profiles() -> None:
    """Test correct profiles."""
    model = CameraModel()
    frame = np.ones((100, 200))
    x_profile, y_profile = model.get_profiles(frame)
    assert x_profile.shape == (200,)
    assert y_profile.shape == (100,)
    assert np.all(x_profile == 1.0)
    assert np.all(y_profile == 1.0)
