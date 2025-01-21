from manim import *

class ZoomScene(MovingCameraScene):
    def construct(self):
        square = Square(color=GREEN)
        self.play(FadeIn(square))
        self.wait(1)

        # Zoom in by a factor of 2
        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.scale(2))
        self.wait(1)

        # Zoom out to original
        self.play(Restore(self.camera.frame))
        self.wait(1)
