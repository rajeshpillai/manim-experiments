from manim import Scene, Square, Circle, Triangle, VGroup, FadeIn, FadeOut, GREEN, BLUE, RED, RIGHT

class MultipleShapesScene(Scene):
    def construct(self):
        # Create shapes
        square = Square(color=GREEN)
        circle = Circle(color=BLUE).next_to(square, RIGHT, buff=1)
        triangle = Triangle(color=RED).next_to(circle, RIGHT, buff=1)

        # Group them together
        shapes = VGroup(square, circle, triangle)

        # Fade in all shapes
        self.play(FadeIn(shapes))
        self.wait(2)

        # Fade out all shapes
        self.play(FadeOut(shapes))
        self.wait(1)
