from manim import *

class ThreeDCameraScene(ThreeDScene):
    def construct(self):
        # Create a sphere
        sphere = Sphere()
        self.play(FadeIn(sphere))
        self.wait(1)

        # Set camera orientation
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.wait(1)

        # Rotate the camera around the sphere
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(5)
        self.stop_ambient_camera_rotation()
