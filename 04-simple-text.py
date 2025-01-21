from manim import Scene, Text, FadeIn, FadeOut

class TextScene(Scene):
    def construct(self):
        # Create a Text mobject
        text = Text("Hello, Manim!", font_size=48)
        self.play(FadeIn(text))
        self.wait(2)
        self.play(FadeOut(text))
