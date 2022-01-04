from manim import *
from manim.utils.scale import LinearBase

class Groupby(Scene):
    def construct(self):
        t0 = Table(
                [
                    ["FB", "Sarah", "350"],
                    ["GOOG", "Sam", "200"],
                    ["MSFT", "Venessa", "124"],
                    ["FB", "Carl", "243"],
                    ["MSFT", "Amy", "340"],
                    ["GOOG", "Charlie", "120"]
                ],
                row_labels=[Text("0"), Text("1"), Text("2"), Text("3"), Text("4"), Text("5")],
                col_labels=[Text('Company'), Text('Person'), Text('Sales')],
                include_outer_lines=True
                )
        code1=Code(code="groupby()", background="rectangle", language="Python", font="Monospace")
        t0.scale(0.7)
        self.play(t0.create())
        self.wait()
        t0.set(v_buff=t0.v_buff*0.7, h_buff=t0.h_buff*0.7)
        self.play(t0.animate.shift(4*LEFT).scale(0.7))
        self.wait()
        self.play(Create(code1))
        self.wait()
        code2=Code(code="groupby(         )", background="rectangle", language="Python", font="Monospace").shift(5*RIGHT + 3*UP).scale(0.5)
        self.play(code1.animate.shift(5*RIGHT, 3*UP).scale(0.5))
        code3 = Code(code="'Company'", background="rectangle", language="Python", font="Monospace", insert_line_no=False)
        self.wait()
        self.play(Create(code3))
        self.play(Circumscribe(t0.get_columns()[1], Rectangle, run_time=3))
        self.play(Transform(code1, code2), code3.animate.scale(0.5).next_to(code2.get_center(), DOWN).shift(0.5*RIGHT))
        code4 = Code(code="groupby('Company')", background="rectangle", language="Python", font="Monospace").shift(5*RIGHT + 3*UP).scale(0.5)
        self.play(Uncreate(code3), Transform(code2, code4))
        self.wait()
        bigrectangle = Rectangle(fill_color=BLACK, fill_opacity=1, stroke_color=YELLOW, width=11, height=3)
        self.play(DrawBorderThenFill(bigrectangle))
        grptxt1 = (
                '<span font_family="monospace"><b><i><span foreground="red">Groupby()</span></i></b> method, unless revoked with an <b><i><span foreground="red">aggregation function</span></i></b>, returns a <b><i><span foreground="red">lazy object</span></i></b>, meaning that no calculation is done until an aggregation function is invoked.</span>'
                )
        justified = MarkupText(grptxt1).move_to(bigrectangle.get_center()).scale_to_fit_width(10.5)
        self.play(Write(justified))
        self.wait(5)
        grptxt2 = (
                '<span font_family="monospace">Lets see what happens when we only call the groupby method.</span>'
                )
        justified2 = MarkupText(grptxt2).move_to(bigrectangle.get_center()).scale_to_fit_width(10.5)
        self.play(Transform(justified, justified2))
        self.wait(2)
        self.play(Unwrite(justified, run_time=2), Uncreate(bigrectangle, run_time=3))
        self.wait()
