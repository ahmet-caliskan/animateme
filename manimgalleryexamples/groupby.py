from manim import *

class Groupby(Scene):
    '''
    Scene is inherited in this class. Will mainly use this for the Scene animation and shenanigans.
    '''
    def construct(self):
        '''
        Animations are done here. Will see how it rolls later on.
        todo
        - add scene sections.
        - carry on to the next stage
        - write proper and clean code
        - figure out delayed simulataneous animations in the same self.play() function.
        '''
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
        self.play(Uncreate(code3, run_time=1), Transform(code2, code4, run_time=1))
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
        def table_column(table: Table, pos: int = 0) -> tuple:
            lastrow = len(t0.get_columns()[pos])
            edge_UL = table.get_cell((1, pos)).get_corner(UP+LEFT)
            edge_UR = table.get_cell((1, pos)).get_corner(UP+RIGHT)
            edge_DL = table.get_cell((lastrow, pos)).get_corner(DOWN+LEFT)
            edge_DR = table.get_cell((lastrow, pos)).get_corner(DOWN+RIGHT)
            return edge_UL, edge_UR, edge_DR, edge_DL
        rec = Polygon(*table_column(t0, 2), stroke_width=10)
        rec.set_opacity=1
        self.play(ShowPassingFlash(rec, run_time=3, time_width=3))
        self.wait()
        self.play(
                t0.animate
                .add_highlighted_cell((2,2), color=TEAL)
                .add_highlighted_cell((5,2), color=TEAL)
                .add_highlighted_cell((3,2), color=RED)
                .add_highlighted_cell((7,2), color=RED)
                .add_highlighted_cell((4,2), color=GOLD)
                .add_highlighted_cell((6,2), color=GOLD)
                )
        self.wait()
        grptxt3 = (
                '<span font_family="monospace">First, the algorithm finds matching instances in the feature that we are grouping by.</span>'
                )
        bigrectangle = Rectangle(fill_color=BLACK, fill_opacity=1, stroke_color=YELLOW, width=11, height=3)
        justified3 = MarkupText(grptxt3).move_to(bigrectangle.get_center()).scale_to_fit_width(10.5)
        self.play(FadeIn(bigrectangle), Write(justified3))
        self.wait(3)
        self.play(FadeOut(bigrectangle, run_time=2), Unwrite(justified3, reverse=True))
        self.wait()
        t1 = Table(
                [
                    ["FB", "Sarah", "350"],
                    ["FB", "Carl", "243"],
                    ["GOOG", "Sam", "200"],
                    ["GOOG", "Charlie", "120"],
                    ["MSFT", "Venessa", "124"],
                    ["MSFT", "Amy", "340"],
                ],
                row_labels=[Text("0"), Text("1"), Text("2"), Text("3"), Text("4"), Text("5")],
                col_labels=[Text('Company'), Text('Person'), Text('Sales')],
                include_outer_lines=True
                )
        t1.scale(0.49)
        t1.shift(4*LEFT)
        t1.add_highlighted_cell((2, 2), color=TEAL).add_highlighted_cell((3, 2), color=TEAL).add_highlighted_cell((4, 2), color=RED).add_highlighted_cell((5, 2), color=RED).add_highlighted_cell((6, 2), color=GOLD).add_highlighted_cell((7, 2), color=GOLD)
        self.play(Transform(t0, t1))
        self.wait(2)
        bigrectangle = Rectangle(fill_color=BLACK, fill_opacity=1, stroke_color=YELLOW, width=11, height=3)
        grptxt4 = (
                '<span font_family="monospace">And then, it groups them together just like that.</span>'
                )
        justified4 = MarkupText(grptxt4).move_to(bigrectangle.get_center()).scale_to_fit_width(10.5)
        self.play(FadeIn(bigrectangle), Write(justified4))
        self.wait(3)
        self.play(FadeOut(bigrectangle, run_time=2), Unwrite(justified4, reverse=True))
        self.wait()
        point1 = t1.get_cell((2, 4)).get_corner(UP+RIGHT)
        point2 = t1.get_cell((3, 4)).get_corner(DOWN+RIGHT)
        brace = BraceBetweenPoints(point1, point2, direction=[1., 0., 0.])
        self.play(Create(brace))
        self.wait()
        gtxt1 = MarkupText('Group1').next_to(brace.get_tip(), RIGHT)
        self.play(Write(gtxt1))
        self.wait()
        point3 = t1.get_cell((3, 4)).get_corner(DOWN+RIGHT)
        point4 = t1.get_cell((5, 4)).get_corner(DOWN+RIGHT)
        brace2 = BraceBetweenPoints(point3, point4, direction=[1., 0., 0.])
        self.play(Create(brace2))
        self.wait()
        gtxt2 = MarkupText('Group2').next_to(brace2.get_tip(), RIGHT)
        self.play(Write(gtxt2))
        self.wait()
        point5 = t1.get_cell((5, 4)).get_corner(DOWN+RIGHT)
        point6 = t1.get_cell((7, 4)).get_corner(DOWN+RIGHT)
        brace3 = BraceBetweenPoints(point5, point6, direction=[1., 0., 0.])
        self.play(Create(brace3))
        self.wait()
        gtxt3 = MarkupText('Group3').next_to(brace3.get_tip(), RIGHT)
        self.play(Write(gtxt3))
        self.wait()
        self.play(Unwrite(gtxt1), Unwrite(gtxt2), Unwrite(gtxt3), Uncreate(brace), Uncreate(brace2), Uncreate(brace3))
        self.wait()
        bigrectangle = Rectangle(fill_color=BLACK, fill_opacity=1, stroke_color=YELLOW, width=11, height=3)
        grptxt5 = (
                '<span font_family="monospace">Keep in mind that this newly created, grouped object is a lazy object.</span>'
                )
        justified5 = MarkupText(grptxt5).move_to(bigrectangle.get_center()).scale_to_fit_width(10.5)
        self.wait()
