from manim import *

class BackgroundColorScene(Scene):
    def construct(self):
        # Set background color to light blue
        self.camera.background_color = "#ADD8E6"

        square = Square(color=GREEN)
        self.play(FadeIn(square))
        self.wait(2)
