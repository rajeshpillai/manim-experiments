from manim import *

class MoveCameraScene(MovingCameraScene):
    def construct(self):
        square = Square(color=GREEN).shift(LEFT * 2)
        self.play(FadeIn(square))
        self.wait(1)

        # Move camera to the right
        self.play(self.camera.frame.animate.shift(RIGHT * 4))
        self.wait(2)
