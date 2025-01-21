from manim import *

class LinearRegressionExplainer(Scene):
    def construct(self):
        self.intro_scene()
        self.plot_data_points()
        self.introduce_regression_line()
        self.show_residuals()
        self.wrap_up()

    def intro_scene(self):
        """
        Scene 1: Intro text about the purpose of linear regression.
        """
        title = Text("Simple Linear Regression", font_size=48)
        subtitle = Text("Explaining the Basics", font_size=24).next_to(title, DOWN)
        self.play(FadeIn(title, shift=UP), FadeIn(subtitle, shift=UP))
        self.wait(2)
        self.play(FadeOut(title, shift=DOWN), FadeOut(subtitle, shift=DOWN))

    def plot_data_points(self):
        """
        Scene 2: Show a coordinate system and data points.
        """
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 10, 1],
            x_length=6,
            y_length=6,
            axis_config={"include_numbers": False},
        )
        axes.center()
        axis_labels = axes.get_axis_labels(
            Tex("X"), Tex("Y")
        )

        self.play(Create(axes), FadeIn(axis_labels))
        self.wait(1)

        # Example data points
        data_points = [(1,2), (2,3.5), (3,2.5), (4,5), (5,6), (6,7.5), (7,7), (8,9)]
        dots = VGroup()
        for x, y in data_points:
            dot = Dot(axes.coords_to_point(x, y), color=BLUE)
            dots.add(dot)

        # Animate the dots appearing
        self.play(
            AnimationGroup(
                *[GrowFromCenter(dot) for dot in dots],
                lag_ratio=0.2
            )
        )
        self.wait(1)

        explanation = Tex(
            "We have data points:\\\\"
            "X = hours of study,\\\\"
            "Y = test scores (for example).",
            font_size=32
        )
        explanation.to_edge(UP)

        self.play(Write(explanation))
        self.wait(3)
        self.play(FadeOut(explanation))

        self.axes = axes
        self.dots = dots

    def introduce_regression_line(self):
        """
        Scene 3 & 4: Introduce a 'searching' line, then settle on best fit.
        """
        # Create a line object that can move around
        initial_line = Line(
            self.axes.coords_to_point(0, 1),
            self.axes.coords_to_point(8, 8),
            color=YELLOW
        )

        self.play(Create(initial_line))
        self.wait(1)

        # Animate it "searching" for the best position
        # We'll do a few random transformations to mimic searching
        self.play(
            initial_line.animate.put_start_and_end_on(
                self.axes.coords_to_point(0, 0),
                self.axes.coords_to_point(8, 5),
            ),
            run_time=2
        )
        self.play(
            initial_line.animate.put_start_and_end_on(
                self.axes.coords_to_point(0, 2),
                self.axes.coords_to_point(8, 6),
            ),
            run_time=2
        )

        # Final best fit line (for demonstration, let's define a known slope + intercept)
        best_fit_line = Line(
            self.axes.coords_to_point(0, 1.5),
            self.axes.coords_to_point(8, 7),
            color=GREEN
        )

        # Transition to best fit line
        self.play(Transform(initial_line, best_fit_line), run_time=2)
        self.wait(1)

        # Show equation
        equation_text = Tex(r"$\hat{y} = \beta_0 + \beta_1 x$", font_size=36)
        equation_text.next_to(self.axes, UP).shift(LEFT*1.5)

        self.play(FadeIn(equation_text))
        self.wait(2)

        self.line = initial_line  # now it's the best fit line

    def show_residuals(self):
        """
        Scene 5 & 6: Show residual lines from points to the regression line.
        """
        residual_lines = VGroup()
        for dot in self.dots:
            # Dot coords
            x_dot, y_dot = self.axes.point_to_coords(dot.get_center())

            # We compute the y on the regression line at x_dot
            # We'll use the final line's slope & intercept from the example:
            # slope ~ (7 - 1.5)/ (8 - 0) = 5.5 / 8 = 0.6875
            # intercept ~ 1.5
            slope = 0.6875
            intercept = 1.5
            y_line = slope * x_dot + intercept

            # Create a line from dot to the line
            start_point = dot.get_center()
            end_point   = self.axes.coords_to_point(x_dot, y_line)
            residual_line = DashedLine(start_point, end_point, color=RED)
            residual_lines.add(residual_line)

        # Animate residual lines appearing
        self.play(LaggedStartMap(Create, residual_lines, lag_ratio=0.1))
        self.wait(2)

        # Optionally, fade them out
        self.play(FadeOut(residual_lines))
        self.wait(1)

    def wrap_up(self):
        """
        Scene 9: Wrap-up text/call to action.
        """
        conclusion = Tex(
            "This is how Simple Linear Regression finds the line \\\\"
            "that best fits your data by minimizing residuals.\\\\"
            "Use it for predictions and insights!",
            font_size=32
        )
        conclusion.to_edge(UP)

        self.play(Write(conclusion))
        self.wait(3)

        # Clear the scene
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()

        # Final text
        thank_you = Text("Thank you for watching!", font_size=48)
        self.play(FadeIn(thank_you, shift=UP))
        self.wait(2)
        self.play(FadeOut(thank_you, shift=DOWN))
