from manim import Scene, Text, FadeIn, FadeOut

class MinimalTestScene(Scene):
    def construct(self):
        title = Text("Minimal Test", font_size=48)
        self.play(FadeIn(title))
        self.wait(2)
        self.play(FadeOut(title))

