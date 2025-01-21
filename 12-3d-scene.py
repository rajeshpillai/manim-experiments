from manim import *

class ThreeDScene(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75*DEGREES, theta=-45*DEGREES)
        cube = Cube(side_length=3, fill_opacity=0.7, fill_color=BLUE)

        self.add(cube)
        self.wait(1)

        # Rotate the cube 45 degrees around the Y-axis
        self.play(Rotate(cube, angle=45 * DEGREES, axis=UP))
        

