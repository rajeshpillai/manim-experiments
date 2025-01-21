from manim import *

class FrameSettingsScene(MovingCameraScene):
    def construct(self):
        # Change frame width and height
        self.camera.frame.width = 14
        self.camera.frame.height = 8

        square = Square(color=GREEN)
        self.play(FadeIn(square))
        self.wait(2)
