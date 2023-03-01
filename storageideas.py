%%manim -pqm -a -v WARNING ExampleRotation

from manim import *

class ExampleRotation(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        m1a = Square().set_color(RED).shift(LEFT)
        m1b = Circle().set_color(RED).shift(LEFT)
        m2a= Square().set_color(BLUE).shift(RIGHT)
        m2b= Circle().set_color(BLUE).shift(RIGHT)

        points = m2a.points
        points = np.roll(points, int(len(points)/4), axis=0)
        m2a.points = points

        # for i in range(4):
        #   m3 = m2a.shift(RIGHT)
        #   self.add(m3)
        #   m2a = m3

        # testers = []
        # for i in range(16):
          # t = Square().set_color(BLUE).shift(RIGHT)
          # points = m2a.points
          # points = np.roll(points, int(len(points)/16), axis=0)
          # m2a.points = points
          # self.add(m2a)

        # self.add(m1a, m2a)
        self.play(Transform(m1a,m1b),Transform(m2a,m2b), run_time=1)

class ExampleRotation(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        m1a = Square().set_color(RED).shift(LEFT)
        m1b = Circle().set_color(RED).shift(LEFT)
        m2a= Square().set_color(BLUE).shift(RIGHT)
        m2b= Circle().set_color(BLUE).shift(RIGHT)

        points = m2a.points
        points = np.roll(points, int(len(points)/4), axis=0)
        m2a.points = points

        self.play(Transform(m1a,m1b),Transform(m2a,m2b), run_time=1)

class ExampleTransform(Scene):
    def construct(self):
        self.camera.background_color = BLACK
        m1 = Square().set_color(RED)
        m2 = Rectangle().set_color(BLUE).set_stroke(width=10).rotate(0.2)
        m3 = Circle(radius=4).set_stroke(width=30).set_color(GREEN)
        self.play(Transform(m1,m2))
        self.play(Transform(m1,m3))

class Count(Animation):
    def __init__(self, number: DecimalNumber, start: float, end: float, **kwargs) -> None:
        # Pass number as the mobject of the animation
        super().__init__(number,  **kwargs)
        # Set start and end
        self.start = start
        self.end = end

    def interpolate_mobject(self, alpha: float) -> None:
        # Set value of DecimalNumber according to alpha
        value = self.start + (alpha * (self.end - self.start))
        self.mobject.set_value(value)


class CountingScene(Scene):
    def construct(self):
        # Create Decimal Number and add it to scene
        number = DecimalNumber().set_color(WHITE).scale(5)
        # Add an updater to keep the DecimalNumber centered as its value changes
        number.add_updater(lambda number: number.move_to(ORIGIN))

        self.add(number)

        self.wait()

        # Play the Count Animation to count from 0 to 100 in 4 seconds
        self.play(Count(number, 0, 10), run_time=4, rate_func=linear)

        self.wait()

class test3(Scene):
    def construct(self):
        square = Square().set_fill(RED, opacity=1.0)
        self.add(square)

        # # animate the change of color
        # self.play(square.animate.set_fill(WHITE))
        # self.wait(1)

        for i in range(3):
          self.play(square.animate.shift(UP).rotate(PI / 3), run_time=0.25)
        for i in range(6):
          self.play(square.animate.shift(DOWN).rotate(PI / 3), run_time=0.25)
        for i in range(3):
          self.play(square.animate.shift(UP).rotate(PI / 3), run_time=0.25)
        self.wait(1)

        # animate the change of position and the rotation at the same time
        for i in range(3):
          self.play(square.animate.shift(UP).rotate(PI / 3))
        for i in range(3):
          self.play(square.animate.shift(DOWN).rotate(PI / 3))
        for i in range(3):
          self.play(square.animate.shift(DOWN).rotate(PI / 3))
        for i in range(3):
          self.play(square.animate.shift(UP).rotate(PI / 3))
        self.wait(1)

class test2(Scene):
    def construct(self):
        squares = []
        sq_ct = 4
        for i in range(sq_ct):
          squares.append(Square(side_length = (i + 1)))
        for i in range(sq_ct):
          squares[i].set_stroke(width= (i + 1) * 2)
        for i in range(sq_ct):
          self.add(squares[i])
        turn = 5
        for i in range(turn):
          self.play(
              squares[0].animate.rotate(PI * 1/turn),
              squares[1].animate.rotate(PI * 2/turn),
              squares[2].animate.rotate(PI * 3/turn),
              squares[3].animate.rotate(PI * 4/turn)
          )

class test1(Scene):
    def construct(self):
        circle = Circle()
        circle.set_stroke(color=BLUE, width=20)
        self.add(circle)
        square = Square().set_stroke(width=10)
        self.add(square)
        for i in range(3):
          self.play(
              square.animate.rotate(PI/3),
              circle.animate.rotate(PI, axis=X_AXIS)
          )

class CreatingMobjects(Scene):
    def construct(self):
        circle = Circle()
        self.add(circle)
        self.wait(1)
        self.remove(circle)
        self.wait(1)

class animatetest(Scene):
    def construct(self):
        circle = Circle()
        self.add(circle)
        square = Square()
        self.add(square)
        for i in range(3):
          self.play(square.animate.rotate(PI/3),
                    circle.animate.rotate(PI, axis=X_AXIS))

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set color and transparency

        square = Square()  # create a square
        square.rotate(PI / 4)  # rotate a certain amount

        self.next_section()
        self.play(Create(square))  # animate the creation of the square
        self.next_section()
        self.play(Transform(square, circle))  # interpolate the square into the circle
        self.next_section()
        self.play(FadeOut(square))  # fade out animation

class AnimatedSquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        square = Square()  # create a square
        self.play(Create(square))  # show the square on screen
        # rotate the square
        self.next_section()
        self.play(
            square.animate.rotate(PI / 4)
        )
        self.next_section()
        self.play(
            ReplacementTransform(square, circle)
        )  # transform the square into a circle
        self.next_section()
        self.play(
            circle.animate.set_fill(PINK, opacity=0.5)
        )  # color the circle on screen

class DifferentRotations(Scene):
    def construct(self):
        left_square = Square(color=RED, fill_opacity=0.7).shift(2 * LEFT)
        right_square = Square(color=GREEN, fill_opacity=0.7).shift(2 * RIGHT)
        # self.play(
        #     left_square.animate.rotate(PI),
        #     Rotate(right_square, angle=PI), run_time=2
        # )
        for i in range(4):
          # self.next_section()
          self.next_section()
          self.play(
              Rotate(left_square, about_point=ORIGIN, angle=PI/2),
              right_square.animate.rotate(PI/2)
          )
          # self.wait(0.1)
