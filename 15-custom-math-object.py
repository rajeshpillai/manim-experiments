from manim import *

class CustomShapeScene(Scene):
    def construct(self):
        # Create a custom shape using VMobject
        custom_shape = VMobject()
        custom_shape.set_points_as_corners([
            ORIGIN, 
            RIGHT, 
            RIGHT + UP, 
            UP, 
            ORIGIN
        ])
        custom_shape.set_color(YELLOW)

        self.play(FadeIn(custom_shape))
        self.wait(2)
