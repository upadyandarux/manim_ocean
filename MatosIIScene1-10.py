# This code was made by Dimas Naufal W.
# With a lil bit of change from Dhimas Upadyandaru

from manimlib import *
import numpy as np

class JUDUL (Scene):
    def construct(self):
        jdl = Text("PDP DIFUSI", t2c={"PDP": TEAL, "DIFUSI": RED},
        font_size=90)
        jdl1 = Text("APA ITU PDP?", t2c={"PDP": TEAL}, font_size=90)
        
        self.play(FadeIn(jdl))
        self.wait(2)
        self.play(ReplacementTransform(jdl, jdl1))
        self.wait(2)

class scene1 (Scene):
    def construct (self):
        komponen = ["x", "y", "z", "w", "=", "(", ")","f"]
        fungsi1 = VGroup(
            Tex("f(x,y) = 0", isolate = [*komponen]),
            Tex("f(x,y,z) = 0", isolate = [*komponen]),
            Tex("f(x,y,z,w) = 0", isolate = [*komponen])
            )
        fungsi1.arrange(DOWN, buff=LARGE_BUFF)
        for line in fungsi1:
            line.set_color_by_tex_to_color_map({
            "x": RED,
            "y": GREEN,
            "z": BLUE,
            "w": ORANGE,
            "0": TEAL,
            "f": TEAL,
            "=": YELLOW
            })
        
        play_1 = {"run_time":2}
        self.play(FadeIn(fungsi1[0]))
        self.wait(1.5)
        self.play(TransformMatchingTex(fungsi1[0].copy(), fungsi1[1]),
            **play_1
        )
        self.wait(1.5)
        self.play(TransformMatchingTex(fungsi1[1].copy(), fungsi1[2]),
            **play_1
        )
        self.wait(1.5)
        self.play(FadeOut(fungsi1))


class scene2 (Scene):
    def construct (self):
        fungsi2 = Tex("{","\\partial u", "\\over" "\\partial t","}", "-", "{", "\\partial{^2}", "{u}", "\\over", "\\partial {x}{^2}","}", "=", "0", "\\text{    }", "\\text{    }", "(1)")
        
        play_2 = {"run_time": 2}
        fungsi2.scale(1.5)
        fungsi2.set_submobject_colors_by_gradient(BLUE, GREEN)
        self.play(Write(fungsi2), **play_2)
        self.wait(2)
        
        arrow1 = Arrow(LEFT,UP)
        arrow2 = Arrow(RIGHT,UP)
        arrow3 = Arrow(LEFT,DOWN)
        arrow4 = Arrow(RIGHT,DOWN)
        
        arrow1.set_color(ORANGE)
        arrow2.set_color(ORANGE)
        arrow3.set_color(ORANGE)
        arrow4.set_color(ORANGE)
        
        arrow1.next_to(fungsi2,DOWN+LEFT)
        arrow2.next_to(fungsi2,DOWN+RIGHT)
        arrow3.next_to(fungsi2,UP+LEFT)
        arrow4.next_to(fungsi2,UP+RIGHT)
        self.play(GrowArrow(arrow1), GrowArrow(arrow2), GrowArrow(arrow3), GrowArrow(arrow4), run_time=1)
        self.wait(1.5)
        self.play(FadeOut(arrow1), FadeOut(arrow2), FadeOut(arrow3), FadeOut(arrow4)) 
        self.play(fungsi2.shift,(2*UP))
        
        sinus = Tex("{", "u", "=", "e{^-}","{^t}", "\\sin", "x", "}")
        sinus.scale(1.5)
        sinus.set_color(TEAL_B)
        sinus.next_to(fungsi2,3*DOWN)
        self.play(ShowCreation(sinus), **play_2)
        self.wait(2)
        self.play(FadeOut(fungsi2), FadeOut(sinus))
        
        fungsi3 = Tex("{","\\partial{^2} u", "\\over" "\\partial t","}", "-", "{", "\\partial{^2}", "{u}","\\over", "\\partial {x}{^2}","}", "=", "0", "\\text{    }", "\\text{    }", "(2)")
        fungsi3.scale(1.5)
        fungsi3.set_submobject_colors_by_gradient(MAROON, PURPLE)
        self.play(DrawBorderThenFill(fungsi3), **play_2)
        self.wait()
        
        arrow1.next_to(fungsi3,DOWN+LEFT)
        arrow2.next_to(fungsi3,DOWN+RIGHT)
        arrow3.next_to(fungsi3,UP+LEFT)
        arrow4.next_to(fungsi3,UP+RIGHT)
        self.play(GrowArrow(arrow1), GrowArrow(arrow2), GrowArrow(arrow3), GrowArrow(arrow4), run_time=1)
        self.wait(1)
        self.play(FadeOut(arrow1), FadeOut(arrow2), FadeOut(arrow3), FadeOut(arrow4)) 
        self.play(fungsi3.shift,(2*UP))
        
        sol = Tex("{", "u", "=", "x{^2}", "-", "y{^2}", "}")
        sol.scale(1)
        sol.set_color(PURPLE)
        sol.next_to(fungsi2,3*DOWN)
        self.play(ShowCreation(sol), **play_2)
        self.wait(2)
        self.play(FadeOut(fungsi3), FadeOut(sol))
        


class scene3 (Scene):
    def construct (self):
        bagian = ["\\partial", "\\varnothing", "x", "y", "A", "B", "C", "D", "E", "F", "G","+","=","\\text{ }"]
        pers = VGroup(
            Tex("{","H(x,y) \\text{ } =","}"),
            Tex("{", "A(x,y) \\text{ }", "{","{\\partial}", "{^2}","{\\varnothing}(x,y) \\over", "{","\\partial {x}","{^2}","}","}","\\text{ }", "+","}", isolate=[*bagian], color=YELLOW_A),
            Tex("{", "B(x,y) \\text{ }", "{","{\\partial}", "{^2}","{\\varnothing}(x,y) \\over", "{","\\partial {y}","{^2}","}","}","\\text{ }", "+","}", isolate=[*bagian], color=YELLOW_B),
            Tex("{", "C(x,y) \\text{ }", "{","{\\partial}", "{\\varnothing}(x,y) \\over", "{","\\partial {x}","}","}","\\text{ }", "+","}", isolate=[*bagian], color=GOLD_A),
            Tex("{", "D(x,y) \\text{ }", "{","{\\partial}", "{\\varnothing}(x,y) \\over", "{","\\partial {y}","}","}","\\text{ }", "+","}", isolate=[*bagian], color=GOLD_B),
            Tex("{", "E(x,y) \\text{ }", "{","{\\partial}", "{^2}","{\\varnothing}(x,y)", "\\over", "{","\\partial {x}","\\partial {y}", "}","}","\\text{ }", "+","}", isolate=[*bagian], color=GOLD_C),
            Tex("{", "F(x,y) \\text{ }", "{","{\\partial}", "{^2}","{\\varnothing}(x,y)", "\\over", "{","\\partial {y}","\\partial {x}", "}","}","\\text{ }", "+","}", isolate=[*bagian], color=LIGHT_BROWN),
            Tex("{", "G(x,y) \\text{ } {\\varnothing(x,y)}\n","}", isolate=[*bagian], color=LIGHT_BROWN)
            )
        
        
        delay = {"run_time":2}
        self.play(pers[0].move_to,(2.5*UP+4*LEFT), **delay)
        pers[1].next_to(pers[0], RIGHT)
        pers[2].next_to(pers[1], RIGHT)
        pers[3].next_to(pers[1], DOWN)
        pers[4].next_to(pers[3], RIGHT)
        pers[5].next_to(pers[3], DOWN)
        pers[6].next_to(pers[5], RIGHT)
        pers[7].next_to(pers[5], DOWN)
        self.play(FadeIn(pers[1]), **delay)
        self.wait(0.5)
        self.play(TransformMatchingTex(pers[1].copy(), pers[2]), **delay)
        self.wait(0.5)
        self.play(TransformMatchingTex(pers[2].copy(), pers[3]), **delay)
        self.wait(0.5)
        self.play(TransformMatchingTex(pers[3].copy(), pers[4]), **delay)
        self.wait(0.5)
        self.play(TransformMatchingTex(pers[4].copy(), pers[5]), **delay)
        self.wait(0.5)
        self.play(TransformMatchingTex(pers[5].copy(), pers[6]), **delay)
        self.wait(0.5)
        self.play(TransformMatchingTex(pers[6].copy(), pers[7]), **delay)
        self.wait(2)
        self.play(Uncreate(pers), **delay)


class scene4 (Scene):
    def construct (self):
        par1 = Text(
            """
            Cara untuk menyelesaikan persamaan diferensial parsial\n
            yang sering dijumpai dalam persoalan fisis, yaitu:
            """,
            font="Arial", font_size=30,
            t2c={"persamaan diferensial parsial": TEAL_B}
        )
        satu = Text("1. Persamaan Laplace,", t2c={"Laplace":YELLOW_A}, font="Arial", font_size=30)
        dua = Text("2. Persamaan difusi,", t2c={"difusi": PURPLE_A}, font="Arial", font_size=30)
        tiga = Text("3. Persamaan gelombang.", t2c={"gelombang": BLUE}, font="Arial", font_size=30)
        difu = VGroup(
            Tex("{", "\\nabla{^2}{u}", "}"),
            Tex(r'='),
            Tex("{", "{", "\\partial{^2}{u}", "\\over", "\\partial{x}{^2}", "\\text{ }", "}", "+","}"),
            Tex("{", "{", "\\partial{^2}{u}", "\\over", "\\partial{v}{^2}", "\\text{ }", "}", "+","}"),
            Tex("{", "{", "\\partial{^2}{u}", "\\over", "\\partial{z}{^2}", "\\text{ }", "}"),
            Tex(r'&='),
            Tex("{", "{", "\\alpha{^2}", "}", "{", "\\partial{u}", "\\over", "\\partial{t}","}", "}")
            )
            
        
        lama={"run_time":2}
        total=VGroup(par1, satu, dua, tiga).arrange(DOWN, buff=0.8)
        self.play(Write(par1), run_time=4)
        self.wait()
        self.play(FadeIn(satu, UP), **lama)
        self.wait()
        self.play(FadeIn(dua,UP), **lama)
        self.wait()
        self.play(FadeIn(tiga,UP), **lama)
        self.wait(2)
        
        difu.set_submobject_colors_by_gradient(YELLOW_A, YELLOW_C)
        new_dua = Text("Persamaan difusi",t2c={"difusi": PURPLE_A}, font="Arial")
        
        last=VGroup(difu, new_dua)
        self.play(TransformMatchingShapes(total, new_dua))
        self.wait(1.5)
        self.play(new_dua.shift,3*UP, **lama)
        difu.arrange(DOWN)
        difu[0].next_to(new_dua, DOWN+0.5*LEFT, buff=1.5)
        difu[1].next_to(difu[0], RIGHT)
        difu[2].next_to(difu[1], RIGHT)
        difu[3].next_to(difu[2], RIGHT)
        difu[4].next_to(difu[3], RIGHT)
        difu[5].next_to(difu[1], DOWN, buff=2)
        difu[6].next_to(difu[5], RIGHT)
        self.play(DrawBorderThenFill(difu))
        self.wait(2)
        self.play(FadeOut(last, RIGHT))
        
        
