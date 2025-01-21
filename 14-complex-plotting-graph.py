from manim import *

class GraphSceneExample(Scene):
    def construct(self):
        # Create axes
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-1, 9, 1],
            axis_config={"color": WHITE},
        )

        # Define the function to plot
        def func(x):
            return x**2

        # Create the graph
        graph = axes.plot(func, color=BLUE)

        # Add axes and graph to the scene
        self.play(FadeIn(axes))
        self.wait(1)
        self.play(FadeIn(graph))
        self.wait(2)

        # Fade out
        self.play(FadeOut(graph), FadeOut(axes))
        self.wait(1)
