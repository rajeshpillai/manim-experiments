from manim import Scene, MathTex, FadeIn, FadeOut

class MathTextScene(Scene):
    def construct(self):
        # Create a MathTex mobject
        equation = MathTex(r"E = mc^2", font_size=72)
        self.play(FadeIn(equation))
        self.wait(2)
        self.play(FadeOut(equation))
