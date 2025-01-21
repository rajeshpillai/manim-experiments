from manim import *

class TextShapeScene(Scene):
    def construct(self):
        # Create a square
        square = Square(color=GREEN)
        self.play(FadeIn(square))
        self.wait(1)

        # Create a text
        text = Text("Square", font_size=24).next_to(square, DOWN)
        self.play(FadeIn(text))
        self.wait(2)

        # Transform the square into a circle with updated text
        circle = Circle(color=BLUE)
        new_text = Text("Circle", font_size=24).next_to(circle, DOWN)
        self.play(Transform(square, circle), Transform(text, new_text))
        self.wait(2)

        # Fade out everything
        self.play(FadeOut(square), FadeOut(text))
        self.wait(1)
