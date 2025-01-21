from manim import *

class MoveTransformScene(Scene):
    def construct(self):
        # Create a square
        square = Square(color=GREEN)
        self.play(FadeIn(square))
        self.wait(1)

        # Define a target position for the square
        square_target = square.copy().shift(RIGHT * 2)
        self.play(square.animate.shift(RIGHT * 2))
        self.wait(1)

        # Transform the square into a circle
        circle = Circle(color=BLUE)
        self.play(Transform(square, circle))
        self.wait(1)

        # Fade out the circle
        self.play(FadeOut(square))
        self.wait(1)
