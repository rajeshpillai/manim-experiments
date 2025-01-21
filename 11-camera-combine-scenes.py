from manim import *

class CameraMovementScene(MovingCameraScene):
    def construct(self):
        # Set background color
        self.camera.background_color = "#F0F8FF"

        # Create a square and circle
        square = Square(color=GREEN).shift(LEFT * 3)
        circle = Circle(color=BLUE).shift(RIGHT * 3)

        self.play(FadeIn(square), FadeIn(circle))
        self.wait(2)

        # Zoom in on the square
        self.play(self.camera.frame.animate.scale(2).move_to(square))
        self.wait(2)

        # Zoom out to show both shapes
        self.play(self.camera.frame.animate.scale(0.5).move_to(ORIGIN))
        self.wait(2)

        # Fade out all
        self.play(FadeOut(square), FadeOut(circle))
        self.wait(1)
