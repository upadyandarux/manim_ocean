#Eigenvalue - Eigenvector Script

#Coders:
    # Dhimas Upadyandaru
    # Michael Bertrand Altawirano Wibisono
    # Zulfikar Kartadimadja
    # Ahmad Al Fauzan

from manimlib.imports import *
from pathlib import Path


#Player
RESOLUTION = " "
FLAGS = f"-pl {RESOLUTION}"
SCENE = "RuangEigenDef"

#INI JUDUL (INTRO)
class Chapter10(LinearTransformationScene):
    CONFIG = {
        "foreground_plane_kwargs" : {
            "x_radius" : FRAME_WIDTH,
            "y_radius" : FRAME_HEIGHT,
            "secondary_line_ratio" : 1

        },
        "include_background_plane" : False,
    }

    def construct(self):
#SLIDE 1
        v_tex = "\\vec{\\textbf{v}}"
        eq = TexMobject("A", v_tex, "=", "\\lambda", v_tex)
        eq.set_color_by_tex(v_tex, YELLOW)
        eq.set_color_by_tex("\\lambda", MAROON_B)
        eq.scale(3)
        eq.add_background_rectangle()
        eq.shift(2*DOWN)

        title = TextMobject(
            "KELOMPOK \\\\",
            "Eigen", "vectors \\\\",
            "Eigen", "values"
        , arg_separator = "")
        title.scale(2)
        title.to_edge(UP)
        # title.set_color_by_tex("Eigen", MAROON_B)
        title[0].set_color(YELLOW)
        title[1].set_color(MAROON_B)
        title[3].set_color(BLUE_D)
        title.add_background_rectangle()


        self.add_vector([-1, 1], color = YELLOW, animate = False)
        self.apply_transposed_matrix([[3, 0], [1, 2]])
        self.plane.fade()
        #self.remove(self.j_hat)
        self.play(Write(title))
        self.wait()
        self.play(Write(eq))
        self.wait()
#SLIDE 2
        title1 = TextMobject("Nama Anggota Kelompok")
        title1.set_color(BLUE)
        title1.scale(2)
        title1.move_to(UP*2)
        title1.add_background_rectangle()
        transform_title1 = TextMobject("Ahmad Al Fauzan \\\\",
                                       "Dhimas Upadyandaru \\\\",
                                       "Michael Bertrand A W \\\\",
                                       "Zulfikar Kartadimaja \\\\")
        transform_title1.set_color(YELLOW)
        transform_title1.next_to(title1,DOWN,buff=1.5)
        transform_title1.scale(1.5)
        transform_title1.add_background_rectangle()
        #self.remove(self.add_vector, self.apply_transposed_matrix, self.plane.fade,
        #            "foreground_plane_kwargs", "include_background_plane")
        self.play(Transform(title,title1))
        self.play(Transform(eq, transform_title1))
        self.wait(5)


# B. Definisi Eigen Value dan Eigen Vector
class ChapterB(Scene):
    def construct(self):
        titleB = TextMobject("DEFINISI") #JUDUL

        #RUMUS
        rms = TextMobject("$Ax = $", "$\lambda$", "$x$")
        lgnd_rms1 = TextMobject("Ax: Vektor berukuran n x n")
        lgnd_rms2 = TextMobject("$\lambda$"," : Skalar elemen real yang memenuhi persamaan, disebut Nilai Eigen (Karakteristik)")
        lgnd_rms2.scale(0.7)
        lgnd_rms3 = TextMobject("$x$"," = Vektor Eigen")
        jabar1 = TextMobject("Misalkan Sebuah Matriks nxn, maka vector", "\\textbf{x}",
                             " yang tidak nol di" , " disebut Vector Eigen (","\\textit{Eigen Vector}", ") dari A jika ",
                             "textbf{Ax}"," adalah kelipatan scalar dari ", "\\textbf{x}", ", yaitu ", "Ax", " = ",
                             "$\\lambda$", "x", " untuk suatu skalar ", "$\\lambda$", ". Skalar ", "$\\lambda$",
                             " dinamakan nilai Eigen (", "$\\textit{Eigen Value}$", ") dari A.")

        titleB.to_corner(UL)
        titleB.set_color(YELLOW)
        rms[1].set_color(YELLOW)
        rms[2].set_color(MAROON_B)
        rms.scale(2)
        rms.shift(2 * UP)
        rms.add_background_rectangle()
        lgnd_rms1.next_to(rms.get_corner(DOWN),DOWN)
        lgnd_rms1.set_color(BLUE_D)
        lgnd_rms2.next_to(lgnd_rms1.get_corner(DOWN), DOWN)
        lgnd_rms2[0].set_color(YELLOW)
        lgnd_rms1.set_color(BLUE_C)
        lgnd_rms3.next_to(lgnd_rms2.get_corner(DOWN), DOWN)
        lgnd_rms3[0].set_color(MAROON_B)
        lgnd_rms1.set_color(BLUE_B)
        jabar1.to_edge(DOWN)

        self.play(Write(titleB))
        self.play(FadeInFromDown(rms))
        self.play(ReplacementTransform(rms.copy(), lgnd_rms1))
        self.play(ReplacementTransform(rms.copy(), lgnd_rms2))
        self.play(ReplacementTransform(rms.copy(), lgnd_rms3))
        self.wait(5)

class visualisasi1(Scene):
    def construct (self):
        dasar=NumberPlane()
        #INTRO
        pnhvecx1 = Vector(np.array([1,3]))
        pjvecx1 = TextMobject("x")
        pnhvecAx1 = Vector(np.array([3,2]))
        pjvecAx1 = TextMobject("Ax")
        pnhvecx2 = Vector(np.array([1,1]))
        pjvecx2 = TextMobject("x")
        pnhvecAx2 = Vector(np.array([4,4]))
        pjvecAx2 = TextMobject("Ax")

        #contoh (a)
        pnhvec11 = Arrow(np.array([-2,-2,0]),np.array([-1,-1,0]),buff=0)
        pjpnh11 = TextMobject("$\lambda$ x")
        pnhvec12 = Arrow(np.array([-2,-2,0]),np.array([2,2,0]),buff=0)
        pjpnh12 = TextMobject("x")
        pja = TextMobject("$0\le \lambda \le 1$")

        #contoh (b)
        pnhvec21 = Arrow(np.array([-2,-2,0]), np.array([2,2,0]), buff=0)
        pjpnh21 = TextMobject("$\lambda$ x")
        pnhvec22 = Arrow(np.array([-2,-2,0]), np.array([-1,-1,0]), buff=0)
        pjpnh22 = TextMobject("x")
        pjb = TextMobject("$\lambda \ge 1$")

        #contoh (c)
        pnhvec31 = Arrow(np.array([-1,-1,0]), np.array([-2,-2,0]), buff=0)
        pjpnh31 = TextMobject("$\lambda$ x")
        pnhvec32 = Arrow(np.array([-1,-1,0]), np.array([2,2,0]), buff=0)
        pjpnh32 = TextMobject("x")
        pjc = TextMobject("$-1\le \lambda \le 0$")

        #contoh (d)
        pnhvec41 = Arrow(np.array([1,1,0]), np.array([-2,-2,0]), buff=0)
        pjpnh41 = TextMobject("$\lambda$ x")
        pnhvec42 = Arrow(np.array([1,1,0]), np.array([2,2,0]), buff=0)
        pjpnh42 = TextMobject("x")
        pjd = TextMobject("$\lambda \le -1$")

        pnhvecx1.set_color(MAROON_B)
        pjvecx1.next_to(pnhvecx1.get_corner(UP), UP)
        pnhvecAx1.set_color(YELLOW)
        pjvecAx1.next_to(pnhvecAx1.get_corner(DOWN), DOWN)
        pnhvecx2.set_color(MAROON_B)
        pjvecx2.next_to(pnhvecx2.get_corner(DOWN), DOWN)
        pnhvecAx2.set_color(YELLOW)
        pjvecAx2.next_to(pnhvecAx2.get_corner(DOWN), DOWN)

        pja.to_edge(UP)
        pja.scale(2)
        pnhvec11.set_color(YELLOW)
        pnhvec12.set_color(BLUE_C)
        pjpnh11.set_color(YELLOW)
        pjpnh12.set_color(BLUE_C)
        pjpnh11.next_to(pnhvec11.get_corner(DOWN), DOWN)
        pjpnh12.next_to(pnhvec12.get_corner(DOWN), DOWN)

        pjb.to_edge(UP)
        pjb.scale(2)
        pnhvec21.set_color(YELLOW)
        pnhvec22.set_color(BLUE_C)
        pjpnh21.set_color(YELLOW)
        pjpnh22.set_color(BLUE_C)
        pjpnh21.next_to(pnhvec21.get_corner(DOWN), DOWN)
        pjpnh22.next_to(pnhvec22.get_corner(DOWN), DOWN)

        pjc.to_edge(UP)
        pjc.scale(2)
        pnhvec31.set_color(YELLOW)
        pnhvec32.set_color(BLUE_C)
        pjpnh31.set_color(YELLOW)
        pjpnh32.set_color(BLUE_C)
        pjpnh31.next_to(pnhvec31.get_corner(DOWN), DOWN)
        pjpnh32.next_to(pnhvec32.get_corner(DOWN), DOWN)

        pjd.to_edge(UP)
        pjd.scale(2)
        pnhvec41.set_color(YELLOW)
        pnhvec42.set_color(BLUE_C)
        pjpnh41.set_color(YELLOW)
        pjpnh42.set_color(BLUE_C)
        pjpnh41.next_to(pnhvec41.get_corner(DOWN), DOWN)
        pjpnh42.next_to(pnhvec42.get_corner(DOWN), DOWN)

        self.add(dasar)
        self.play(GrowArrow(pnhvecx1))
        self.play(GrowArrow(pnhvecAx1))
        self.play(FadeInFromDown(pjvecx1), FadeInFromDown(pjvecAx1))
        self.play(FadeOut(pnhvecx1), FadeOut(pnhvecAx1), FadeOut(pjvecx1), FadeOut(pjvecAx1))
        self.play(GrowArrow(pnhvecx2))
        self.play(GrowArrow(pnhvecAx2))
        self.play(FadeInFromDown(pjvecx2), FadeInFromDown(pjvecAx2))
        self.play(FadeOut(pnhvecx1), FadeOut(pnhvecAx1), FadeOut(pjvecx1), FadeOut(pjvecAx1))
        self.wait()

        self.add(dasar)
        self.play(Write(pja))
        self.play(GrowArrow(pnhvec11))
        self.play(FadeInFromDown(pjpnh11))
        self.play(GrowArrow(pnhvec12))
        self.play(FadeInFromDown(pjpnh12))
        self.play(FadeOut(pnhvec11), FadeOut(pnhvec12), FadeOut(pjpnh11), FadeOut(pjpnh12))
        self.play(FadeOut(pja), Transform(pja,pjb))
        self.play(GrowArrow(pnhvec21))
        self.play(FadeInFromDown(pjpnh21))
        self.play(GrowArrow(pnhvec22))
        self.play(FadeInFromDown(pjpnh22))
        self.play(FadeOut(pnhvec21), FadeOut(pnhvec22), FadeOut(pjpnh21), FadeOut(pjpnh22))
        self.play(FadeOut(pjb), Transform(pjb, pjc))
        self.play(GrowArrow(pnhvec31))
        self.play(FadeInFromDown(pjpnh31))
        self.play(GrowArrow(pnhvec32))
        self.play(FadeInFromDown(pjpnh32))
        self.play(FadeOut(pnhvec31), FadeOut(pnhvec32), FadeOut(pjpnh31), FadeOut(pjpnh32))
        self.play(FadeOut(pjc), Transform(pjc, pjd))
        self.play(GrowArrow(pnhvec41))
        self.play(FadeInFromDown(pjpnh41))
        self.play(GrowArrow(pnhvec42))
        self.play(FadeInFromDown(pjpnh42))
        self.play(FadeOut(pnhvec41), FadeOut(pnhvec42), FadeOut(pjpnh41), FadeOut(pjpnh42), FadeOut(pjd))
        self.wait()

#Ini Persamaan Karakteristik
class PersamaanKarakteristik(Scene):
    def construct(self):
        titlePK = TextMobject("\\textbf{Persamaan Karakteristik A}")
        titlePK.set_color(YELLOW)
        titlePK.to_edge(UP, buff=1)
        eq1 = TextMobject("$Ax=\lambda x$")
        pjeq1 = TextMobject("Persamaan EIGENVECTOR dan EIGENVALUES $A$")
        eq2 = TextMobject("$\left( A-\lambda I \\right) x=0$")
        eq3 = TextMobject("$\left| A-\lambda I \\right| = 0$")
        pjeq3 = TextMobject("Untuk setiap Nilai Eigen $\left( \lambda  \\right)$ \\\\",
                            "HARUS memenuhi Persamaan:")

        eq1.scale(2)
        eq1.add_background_rectangle(color=YELLOW)
        pjeq1.next_to(eq1,DOWN)
        eq2.scale(2)
        eq2.add_background_rectangle(color=YELLOW)
        pjeq3.next_to(eq2,UP)
        eq3.scale(2)
        eq3.add_background_rectangle(color=BLUE_C)
        eq3.next_to(pjeq3, DOWN)

        self.play(Write(titlePK))
        self.play(Write(eq1), Write(pjeq1))
        self.play(Transform(eq1, eq2))
        self.play(Transform(eq2, pjeq3))
        self.remove(eq1)
        self.play(Transform(pjeq1, eq3),)
        self.play(FadeOut(eq3), FadeOut(pjeq3), FadeOut(titlePK))
        self.wait(8)


#Perhitungan EigenValues dan EigenVector
class PerhitunganEigen(Scene):
    def construct(self):
        #untuk EigenValues
        titleval = TextMobject("PERHITUNGAN EIGENVALUES")

        introval = TextMobject("Dengan Meninjau Perkalian MATRIKS A dan X dengan MATRIKS Identitas pada kedua sisi \\\\",
                               "Maka Didapatkan:")
        eqval1 = TextMobject("$IAX=I\lambda X$")
        arrow1 = Arrow(LEFT)
        eqval2 = TextMobject("$AX=\lambda X$")
        eqval3 = TextMobject("$\left[ \lambda I-A \\right] X=0$")
        pjval3 = TextMobject("Namun Persamaan tersebut dapat Terpenuhi JIKA dan HANYA JIKA")
        eqvaldet = TextMobject("$det\left[ \lambda I-A \\right]$")
        pjval4 = TextMobject("Sehingga Nilai Eigen $\left( \lambda  \\right)$ dari Matriks Bujur Sangkar A dapat ditentukan")

        titleval.set_color(YELLOW)
        titleval.to_edge(UP, buff=1)
        introval.next_to(titleval, DOWN, buff=1)
        introval.scale(0.7)
        arrow1.next_to(introval, DOWN)
        eqval1.next_to(arrow1, 1*LEFT)
        eqval2.next_to(arrow1, 1*RIGHT)
        eqval3.next_to(introval, DOWN)
        eqval3.add_background_rectangle(color=YELLOW)
        pjval3.next_to(eqval3, DOWN)
        pjval3.scale(0.7)
        eqvaldet.next_to(pjval3, DOWN)
        eqvaldet.add_background_rectangle(color=YELLOW)
        pjval4.next_to(eqvaldet, DOWN)
        pjval4.scale(0.7)

        #untuk EigenVector
        titlevec1 = TextMobject("PERHITUNGAN EIGENVECTOR")

        eqvecin = TextMobject("$Ax=\lambda x$")
        pjvecin1 = TextMobject("$A=$ Matriks Bujur Sangkar")
        pjvecin2 = TextMobject("$X=$ Vektor BUKAN nol yang memenuhi Persamaan")

        titlevec2 = TextMobject("VEKTOR EIGEN")

        eqvec1 = TextMobject(r"$A=\begin{bmatrix} { a }_{ 11 } \ { a }_{ 21 } \\ { a }_{ 12 } \ { a }_{ 22 } \end{bmatrix}$")
        eqvec2 = TextMobject("untuk $Ax=\lambda x$")
        eqvec2a = TextMobject(r"$\begin{bmatrix} { a }_{ 11 } \ { a }_{ 21 } \\ { a }_{ 12 } \ { a }_{ 22 } \end{bmatrix} \begin{bmatrix} { x }_{ 1 } \\ { x }_{ 2 } \end{bmatrix}=\lambda \begin{bmatrix} { x }_{ 1 } \\ { x }_{ 2 } \end{bmatrix}$")
        pjvec3 = TextMobject("Dikalikan dengan Matriks Identitas")
        eqvec31 = TextMobject(r"$\begin{bmatrix} 1 \ 0 \\ 0 \ 1 \end{bmatrix} \begin{bmatrix} { a }_{ 11 } \ { a }_{ 21 } \\ { a }_{ 12 } \ { a }_{ 22 } \end{bmatrix} \begin{bmatrix} { x }_{ 1 } \\ { x }_{ 2 } \end{bmatrix}=\lambda \begin{bmatrix} 1 \ 0 \\ 0 \ 1 \end{bmatrix} \begin{bmatrix} { x }_{ 1 } \\ { x }_{ 2 } \end{bmatrix}$")
        eqvec32 = TextMobject(r"$\begin{bmatrix} { a }_{ 11 } \ { a }_{ 21 } \\ { a }_{ 12 } \ { a }_{ 22 } \end{bmatrix} \begin{bmatrix} { x }_{ 1 } \\ { x }_{ 2 } \end{bmatrix}= \begin{bmatrix} \lambda \ 0 \\ 0 \ \lambda \end{bmatrix} \begin{bmatrix} { x }_{ 1 } \\ { x }_{ 2 } \end{bmatrix}$")
        eqvec33 = TextMobject(r"$\begin{bmatrix} { a }_{ 11 }-\lambda \ { a }_{ 12 } \\ { a }_{ 21 } \ { a }_{ 22 }-\lambda \end{bmatrix} \begin{bmatrix} { x }_{ 1 } \\ { x }_{ 2 } \end{bmatrix}=0$")
        pjvec4 = TextMobject("Dapat juga dituliskan Sebagai Persamaan Linier sebagai: ")
        eqvec41 = TextMobject("$\left( { a }_{ 11 }-\lambda \\right) { x }_{ 1 }+{ a }_{ 12 }{ x }_{ 2 }=0$")
        eqvec42 = TextMobject("${ a }_{ 21 }{ x }_{ 1 }+\left( { a }_{ 22 }-\lambda \\right) { x }_{ 2 }=0$")
        groupeqvec2 = VGroup(eqvec2, eqvec2a)

        titlevec1.set_color(YELLOW)
        titlevec1.to_edge(UP, buff=1)
        eqvecin.next_to(titlevec1, DOWN, buff=2)
        eqvecin.add_background_rectangle(color=RED_C,opacity=1)
        eqvecin.scale(2)
        pjvecin1.next_to(eqvecin, 1*DOWN)
        pjvecin1.set_color(RED_D)
        pjvecin2.next_to(pjvecin1, 1*DOWN)
        pjvecin2.set_color(TEAL_C)
        titlevec2.set_color(YELLOW)
        titlevec2.to_edge(UP, buff=1)
        eqvec1.shift(1*UP)
        eqvec2a.next_to(eqvec2, DOWN)
        groupeqvec2.next_to(eqvec1, DOWN)
        pjvec3.next_to(titlevec2, 1.5*DOWN)
        eqvec31.next_to(pjvec3, 1*DOWN)
        eqvec32.next_to(eqvec31, 1*DOWN)
        eqvec33.next_to(eqvec32, 1*DOWN)
        pjvec4.next_to(titlevec2, 2 * DOWN)
        eqvec41 .next_to(pjvec4, 1.25 * DOWN)
        eqvec42 .next_to(eqvec41, 1.25 * DOWN)

        #EValues
        self.play(Write(titleval))
        self.play(Write(introval))
        self.play(FadeIn(eqval1))
        self.play(GrowArrow(arrow1))
        self.play(FadeIn(eqval2))
        self.play(FadeOut(eqval1), FadeOut(arrow1))
        self.wait(1)
        self.play(Transform(eqval2, eqval3), FadeIn(eqvaldet))
        self.play(
            ReplacementTransform(eqval3.copy(), pjval3),
            ReplacementTransform(eqvaldet.copy(), pjval4)
        )
        self.wait(3)
        self.remove(eqval2)
        self.play(FadeOut(introval), FadeOut(pjval3), FadeOut(eqvaldet), FadeOut(pjval4))
        self.remove(titleval)
        self.wait(2)
        
        #EVector
        self.play(Write(titlevec1))
        self.play(Write(eqvecin))
        self.play(
            ReplacementTransform(eqvecin.copy(), pjvecin1),
            ReplacementTransform(eqvecin.copy(), pjvecin2)
        )
        self.wait(3)
        self.play(Transform(titlevec1, titlevec2))
        self.remove(eqvecin)
        self.wait(2)
        self.play(Transform(pjvecin1, eqvec1))
        self.play(Transform(pjvecin2, groupeqvec2))
        self.wait(3)
        self.play(
            FadeOutAndShift(eqvec1, direction=UP),
            FadeOutAndShift(groupeqvec2, direction=UP)
        )
        self.remove(pjvecin1)
        self.remove(pjvecin2)

        self.play(Write(pjvec3))
        self.play(ReplacementTransform(pjvec3.copy(), eqvec31))
        self.play(ReplacementTransform(eqvec31.copy(), eqvec32))
        self.play(ReplacementTransform(eqvec32.copy(), eqvec33))
        self.wait(3)
        self.play(FadeOutAndShift(eqvec31, direction=UP),
                  FadeOutAndShift(eqvec32, direction=UP),
                  FadeOutAndShift(eqvec33, direction=UP))
        self.play(Transform(pjvec3, pjvec4))
        self.play(ReplacementTransform(pjvec4.copy(), eqvec41))
        self.play(ReplacementTransform(eqvec41.copy(), eqvec42))
        self.wait(3)
        self.play(FadeOut(pjvec4), FadeOut(eqvec41), FadeOut(eqvec42))
        self.remove(titlevec1)
        self.remove(pjvec3)
        self.remove(eqvec41)
        self.remove(eqvec42)
        self.wait(3)


class contohsoal1(Scene):
    def construct (self):
        jdlsoal = TextMobject("CONTOH SOAL")
        snum1 = TextMobject("1. Buktikan vektor $x=\left( 2,-1 \\right)$ adalah Vektor Eigen dari $A=\left[ \left( 1,4 \\right) ,\left( 2,3 \\right)  \\right] $ dan tentukan Nilai Eigennya!")
        pjjwb1 = TextMobject("Dibuktikan dengan cara Mengalikan Matriks dengan Vektornya")
        jwbnum11 = TextMobject(r"$ Ax=\begin{bmatrix} 1 \ 4 \\ 2 \ 3 \end{bmatrix} \begin{bmatrix} 2 \\ -1 \end{bmatrix}=\begin{bmatrix} -2 \\ 1 \end{bmatrix}=$") 
        jwbnum12 = TextMobject("$ -1 $")
        pjnum12 = TextMobject("\\tiny NILAI EIGEN")
        arrow12 = Arrow(UP)
        jwbnum13 = TextMobject(r"$\begin{bmatrix} 2 \\ -1 \end{bmatrix}$")
        pjnum13 = TextMobject("\\tiny VEKTOR EIGEN")
        arrow13 = Arrow(LEFT)

        jdlsoal.to_edge(UP)
        snum1.next_to(jdlsoal, DOWN)
        snum1.scale(0.7)
        pjjwb1.next_to(snum1, DOWN)
        pjjwb1.scale(0.7)
        jwbnum11.shift(3*LEFT)
        jwbnum12.next_to(jwbnum11, RIGHT)
        arrow12.next_to(jwbnum12, DOWN)
        pjnum12.next_to(arrow12, DOWN)
        jwbnum12.set_color(RED_C)
        arrow12.set_color(RED_C)
        arrow12.scale(0.7)
        pjnum12.set_color(RED_C)
        jwbnum13.next_to(jwbnum12, RIGHT)
        arrow13.next_to(jwbnum13, RIGHT)
        arrow13.scale(0.7)
        pjnum13.next_to(arrow13, RIGHT)
        jwbnum13.set_color(YELLOW_B)
        arrow13.set_color(YELLOW_B)
        pjnum13.set_color(YELLOW_B)

        self.play(Write(jdlsoal))
        self.play(Write(snum1))
        self.wait(3)
        self.play(Write(pjjwb1))
        self.wait(1)
        self.play(Write(jwbnum11))
        self.play(FadeInFromDown(jwbnum12), FadeInFromDown(jwbnum13))
        self.wait(1)
        self.play(GrowArrow(arrow12), GrowArrow(arrow13))
        self.play(Write(pjnum12))
        self.play(Write(pjnum13))
        self.play(FadeOut(jwbnum11), FadeOut(pjnum12), FadeOut(jwbnum12), FadeOut(pjnum13), FadeOut(jwbnum13), FadeOut(arrow12),
                  FadeOut(arrow13), FadeOut(pjjwb1))
        self.remove(snum1)
        self.wait(3)


        snum2 = TextMobject(r"2. Sebuah vektor $X=\begin{bmatrix} 2 \\ 1 \end{bmatrix}$ dan sebuah matriks $A=\begin{bmatrix} 1 \ 4 \\ 0 \ 3 \end{bmatrix}$")
        jwbnum21 = TextMobject("Ketika Matriks $A$ dikalikan dengan $X$ akan Didapatkan: ")
        jwbnum22a = TextMobject(r"$AX=\begin{bmatrix} 1 \ 4 \\ 0 \ 3 \end{bmatrix} \begin{bmatrix} 2 \\ 1 \end{bmatrix}= \begin{bmatrix} 2+4 \\ 0+3 \end{bmatrix}=$")
        jwbnum22b = TextMobject(r"$\begin{bmatrix} 6 \\ 3 \end{bmatrix}$")
        groupnum22 = VGroup(jwbnum22a, jwbnum22b)
        pjnum23a = TextMobject("Dimana: ")
        arrow23 = Arrow(UP)
        pjnum23b = TextMobject(r"$\begin{bmatrix} 6 \\ 3 \end{bmatrix}$ = 3$\begin{bmatrix} 2 \\ 1 \end{bmatrix}=\lambda X$")
        pjnum24 = TextMobject(r"Nilai Eigen dari Matriks $A=\begin{bmatrix} 1 \ 4 \\ 0 \ 3 \end{bmatrix}$")
        jwbnum24a = TextMobject("$EigenValue $","$ (\lambda) = 3$")

        snum2.next_to(jdlsoal, DOWN)
        snum2.scale(0.7)
        jwbnum21.next_to(snum2, DOWN)
        jwbnum21.scale(0.7)
        jwbnum22a.shift(0.5*LEFT)
        jwbnum22b.next_to(jwbnum22a, RIGHT)
        pjnum23a.next_to(jwbnum22a, LEFT + DOWN)
        pjnum23a.shift(1.1*RIGHT)
        pjnum23a.scale(0.7)
        pjnum23b.next_to(pjnum23a, 1*RIGHT + DOWN)
        pjnum24.shift(UP)
        pjnum24.scale(0.7)
        jwbnum24a.next_to(pjnum24.get_corner(DOWN), DOWN)
        jwbnum24a.scale(0.7)
        jwbnum24a.generate_target()
        jwbnum24a.target.shift(UP)

        self.play(Write(snum2))
        self.play(Write(jwbnum21))
        self.play(FadeInFromDown(jwbnum22a), FadeInFromDown(jwbnum22b))
        self.play(Write(pjnum23a))
        self.play(FadeInFromDown(pjnum23b))
        self.wait(2)
        self.play(FadeOut(jwbnum21), FadeOut(jwbnum22a), FadeOut(jwbnum22b), FadeOut(pjnum23a), FadeOut(pjnum23b))
        self.play(Transform(snum2, pjnum24))
        self.play(ReplacementTransform(pjnum24.copy(), jwbnum24a))
        self.play(FadeOut(jwbnum24a), FadeOut(snum2), FadeOut(jdlsoal))
        self.wait(5)

        
        
#Ruang Eigen
class RuangEigenDef(Scene):
    def construct (self):
        jdlre = TextMobject("RUANG EIGEN")
        pjinre1 = TextMobject("Untuk Mencari VEKTOR EIGEN yang Sesuai")
        pjinre21 = TextMobject("VEKTOR EIGEN yang bersesuaian dengan \\\\",
                               "NILAI EIGEN $\lambda$")
        pjinre22 = TextMobject("$vektor\\neq 0$ dalam Ruang Penyelesaian $\left( \lambda I-A \\right) x=0$")
        pjinre31 = TextMobject("Ruang Penyelesaian \\\\",
                               "dari Sistem Linear \\\\",
                               "$\left( \lambda I-A \\right) x=0$")
        pjinre32 = TextMobject("EIGEN SPACE")
        pjinre33 = TextMobject("dari $Matriks\quad A$ (ukuran $n\\times n$)")

        jdlre.to_edge(UP)
        jdlre.set_color(YELLOW)
        jdlre.scale(2)
        #pjinre1 Biarin di Tengah Lokasinya
        pjinre21.shift(0.5*UP)
        pjinre22.next_to(pjinre21.get_corner(DOWN), DOWN)
        pjinre31.scale(1)
        pjinre31.shift(UP)
        pjinre32.scale(1.5)
        pjinre32.next_to(pjinre31.get_corner(DOWN), DOWN)
        pjinre32.set_color(RED)
        pjinre32.generate_target()
        pjinre32.target.shift(0.5 * UP)
        pjinre33.next_to(pjinre32.get_corner(DOWN), DOWN)

        self.play(Write(jdlre))
        self.play(Write(pjinre1))
        self.play(ReplacementTransform(pjinre1, pjinre21))
        self.play(FadeInFromDown(pjinre22))
        self.wait(2)
        self.play(Transform(pjinre21, pjinre31), Transform(pjinre22, pjinre32))
        self.wait(2)
        self.remove(jdlre,pjinre21,pjinre22)
        self.play(MoveToTarget(pjinre32))
        self.play(ReplacementTransform(pjinre32.copy(), pjinre33))
        self.wait(3)
        self.play(FadeOut(jdlre), FadeOut(pjinre32), FadeOut(pjinre33))
        self.wait(1)

#Teorema 5.2 dan 5.3
class teorema(Scene):
    def construct(self):
        title_1 = TextMobject("Teorema 5.2")
        teks1_1 = TextMobject("Jika ","${S}_{A} \left( \lambda \\right)$"," adalah ruang eigen dari matriks A berukuran m x m yang bersesuaian dengan ","$\lambda$")
        teks1_2 = TextMobject("maka ","${S}_{A} \left( \lambda \\right)$"," adalah sub ruang vector dari R")
    
        title_2 = TextMobject("Pembuktian Teorema 5.2")
        teks2_1 = TextMobject("Dengan menggunakan definisi:")
        teks2_2 = TextMobject("Jika $x \in S_{A} \left( \lambda \\right)$, maka $Ax = \lambda x$")
        teks2_3 = TextMobject("Maka jika ","$x \in S_{A} \left( \lambda \\right)$"," dan ","$y \in S_{A}\left( \lambda \\right)$",", \\\\ maka untuk skalar ","a"," dan ","B"," berlaku:")
        eq2_1 = TexMobject(r"A\left( a x+B y \right)")
        eq2_2 = TexMobject(r"=a Ax+B Ay")
        eq2_3 = TexMobject(r"=a \left( \lambda x \right) +B \left( \lambda y \right) ")
        eq2_4 = TexMobject(r"=\lambda \left( a x+B y \right) ")
        teks2_4 = TextMobject("Akibatnya ","$\left( ax+By \\right) \in {S}_{A} \left( \lambda \\right)$"," dan ","${S}_{A}\left( \lambda \\right)$"," merupakan ruang vektor")

        title_1.to_edge(UP, buff=1)
        teks1_1.next_to(title_1, 4*DOWN)
        teks1_1.scale(0.7)
        teks1_1[1].set_color(YELLOW)
        teks1_1[3].set_color(RED)
        teks1_2.next_to(teks1_1, 2*DOWN)
        teks1_2.scale(0.7)
        teks1_2[1].set_color(YELLOW)

        title_2.to_edge(UP, buff=1)
        teks2_1.next_to(title_2, 4*DOWN)
        teks2_1.scale(0.7)
        teks2_2.next_to(teks2_1, 2*DOWN)
        teks2_2.scale(0.7)
        teks2_2.set_color(YELLOW)
        teks2_3.next_to(title_2, 3*DOWN)
        teks2_3.scale(0.7)
        teks2_3[1].set_color(YELLOW)
        teks2_3[3].set_color(GREEN)
        teks2_3[5].set_color(YELLOW)
        teks2_3[7].set_color(RED_C)
        eq2_1.next_to(teks2_3, 2*DOWN)
        eq2_1.shift(1.5*LEFT)
        eq2_1.set_color(RED)
        eq2_2.next_to(eq2_1, RIGHT)
        eq2_2.set_color(BLUE)
        eq2_3.next_to(eq2_1, RIGHT)
        eq2_3.set_color(YELLOW)
        eq2_4.next_to(eq2_1, RIGHT)
        eq2_4.set_color(TEAL)
        teks2_4.next_to(teks2_3, 6*DOWN)
        teks2_4.scale(0.7)
        teks2_4[1].set_color(YELLOW)
        teks2_4[3].set_color(MAROON_B)
        
        self.play(Write(title_1))
        self.play(Write(teks1_1))
        self.play(Write(teks1_2))
        self.wait(8)
        self.play(ReplacementTransform(title_1, title_2))
        self.play(ReplacementTransform(teks1_1, teks2_1))
        self.play(ReplacementTransform(teks1_2, teks2_2))
        self.wait(2)
        self.play(FadeOut(teks2_1), FadeOut(teks2_2))
        self.play(ReplacementTransform(teks2_2.copy(), teks2_3))
        self.play(Write(eq2_1))
        self.play(ReplacementTransform(eq2_1.copy(), eq2_2))
        self.wait(2)
        self.play(ReplacementTransform(eq2_2, eq2_3))
        self.wait(2)
        self.play(ReplacementTransform(eq2_3, eq2_4))
        self.wait(2)
        self.play(ReplacementTransform(eq2_1.copy(), teks2_4))
        self.wait(6)
        self.remove(title_2, teks2_3, teks2_4, eq2_1, eq2_4)
        self.wait(2)
       
class teorema3(Scene):
    def construct(self):
        judul = TextMobject("Teorema 5.3")
        teks = TextMobject("Jika diberikan matriks ${A}_{m x m}$. Maka,")
        point1 = TextMobject("a) Eigenvalue ${A}^{T}$ adalah sama dengan eigenvalue A.")
        point2 = TextMobject("b) A matriks singular jika dan hanya jika sedikitnya satu eigenvalue A sama dengan 0.")
        point3 = TextMobject("c) Elemen-elemen diagonal A adalah eigenvalue A, jika A merupakan matriks segitiga.")
        point4 = TextMobject("d) Eigenvalue $BA{B}^{-1}$ sama dengan eigenvalue A, jika B merupakan matriks nonsingular m x m.")
        point5 = TextMobject("e) Setiap eigenvalue A adalah +1 atau -1, jika A merupakan matriks orthogonal.")
        
        judul.to_edge(UP, buff=1)
        teks.next_to(judul, 2*DOWN)
        teks.scale(0.85)
        point1.align_to(teks, RIGHT)
        point1.shift(1*UP)
        point1.scale(0.7)
        point2.next_to(point1, DOWN)
        point2.scale(0.7)
        point2.shift(1.85*RIGHT)
        point3.next_to(point2, DOWN)
        point3.scale(0.7)
        point3.shift(0.1*RIGHT)
        point4.arrange(DOWN, center=False, aligned_edge=LEFT)  
        point4.shift(0.5*UP + 0.25*LEFT)
        point4.scale(0.7)
        point5.next_to(point4, DOWN)
        point5.shift(0.65*LEFT)
        point5.scale(0.7)
        
        self.play(Write(judul))
        self.play(Write(teks))
        self.play(Write(point1))
        self.wait(2)
        self.play(Write(point2))
        self.wait(2)
        self.play(Write(point3))
        self.wait(2)
        self.play(
            FadeOut(point1),
            FadeOut(point2),
            FadeOut(point3)
            )
        self.play(Write(point4))
        self.wait(2)
        self.play(Write(point5))
        self.wait(2)
        self.play(
            FadeOut(judul),
            FadeOut(teks),
            FadeOut(point4),
            FadeOut(point5)
            )


class contohsoal2(Scene):
    def construct (self):
        judul = TextMobject("CONTOH SOAL")
        soal1 = TextMobject("1. Carilah nilai-nilai eigen dan basis-basis untuk ruang eigen \\\\ dari A = [(3,2),(-1,0)]")
        jawaban1_1 = TextMobject("det($\lambda$I-A)=0")
        panah1 = Arrow(LEFT).scale(1)
        jawaban1_2 = TextMobject("$\lambda$I-A")
        jawaban1_3 = TexMobject(r"=\lambda \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}-\begin{bmatrix} 3 & 2 \\ -1 & 0 \end{bmatrix}")
        jawaban1_4 = TexMobject(r"=\begin{bmatrix} \lambda -3 & -2 \\ 1 & \lambda  \end{bmatrix}")
        jawaban1_5 = TextMobject("($\lambda$-3)($\lambda$)-(-1)(2)=0")
        jawaban1_6 = TextMobject("${\lambda}^{2}-3 \lambda $+2=0")
        jawaban1_7 = TextMobject("$\left( \lambda -2 \\right) \left( \lambda -1 \\right)=0$")
        jawaban1_8 = TextMobject("Maka didapatkan nilai eigen:")
        jawaban1_9 = TextMobject("${\lambda}_{1}$ =2, ${\lambda}_{2}$ = 1")

        judul.to_edge(UP, buff=1)
        soal1.next_to(judul, 2*DOWN)
        panah1.next_to(soal1, 2*DOWN)
        jawaban1_1.next_to(panah1, LEFT)
        jawaban1_2.next_to(panah1, RIGHT)
        jawaban1_3.next_to(jawaban1_2, RIGHT)
        jawaban1_4.next_to(jawaban1_2, RIGHT)
        jawaban1_5.next_to(jawaban1_1, DOWN)
        jawaban1_6.next_to(jawaban1_1, DOWN)
        jawaban1_7.next_to(jawaban1_1, DOWN)
        jawaban1_8.next_to(panah1, 5*DOWN)
        jawaban1_9.next_to(jawaban1_8, DOWN)

        self.play(FadeIn(judul))
        self.play(Write(soal1))
        self.play(FadeIn(jawaban1_1))
        self.play(Write(panah1), Write(jawaban1_2))
        self.play(ReplacementTransform(jawaban1_2.copy(), jawaban1_3))
        self.play(ReplacementTransform(jawaban1_3, jawaban1_4))
        self.play(FadeIn(jawaban1_5))
        self.play(ReplacementTransform(jawaban1_5, jawaban1_6))
        self.play(ReplacementTransform(jawaban1_6, jawaban1_7))
        self.play(Write(jawaban1_8))
        self.play(ReplacementTransform(jawaban1_8.copy(), jawaban1_9))

        jawaban1_10 = TextMobject("Ruang vektor:")
        jawaban1_11 = TexMobject(r"\begin{bmatrix} \lambda -3 & -2 \\ 1 & \lambda  \end{bmatrix}\begin{bmatrix} { x }_{ 1 } \\ { x }_{ 2 } \end{bmatrix}=\begin{bmatrix} 0 \\ 0 \end{bmatrix}")
        jawaban1_12 = TextMobject("Untuk ${\lambda}_{1}=2$ diperoleh:")
        jawaban1_13 = TexMobject(r"\begin{bmatrix} -1 & -2 \\ 1 & 2 \end{bmatrix}\begin{bmatrix} { x }_{ 1 } \\ { x }_{ 2 } \end{bmatrix}=\begin{bmatrix} 0 \\ 0 \end{bmatrix}")
        panah2 = Arrow(LEFT).scale(1)
        jawaban1_14 = TextMobject("${-x}_{1}-{2x}_{2}=0$ \\\\ ${x}_{1}+{2x}_{2}=0$")
        panah3 = Arrow(UP).scale(1)
        jawaban1_15 = TextMobject("${x}_{1}=-2{x}_{2}$")
        
        jawaban1_10.next_to(panah1, LEFT)
        jawaban1_11.next_to(jawaban1_10, RIGHT)
        jawaban1_12.next_to(panah1, 3*DOWN)
        panah2.next_to(jawaban1_12, 3*DOWN)
        jawaban1_13.next_to(panah2, LEFT)
        jawaban1_14.next_to(panah2, RIGHT)
        panah3.next_to(jawaban1_14, DOWN)
        jawaban1_15.next_to(panah3, DOWN)
        
        self.play(
            ReplacementTransform(jawaban1_1,jawaban1_10),
            ReplacementTransform(jawaban1_2,jawaban1_11),
            FadeOut(panah1),
            FadeOut(jawaban1_4),
            FadeOut(jawaban1_7),
            FadeOut(jawaban1_8),
            FadeOut(jawaban1_9)
        )
        self.play(FadeIn(jawaban1_12))
        self.play(ReplacementTransform(jawaban1_12.copy(), jawaban1_13))
        self.play(
            Write(panah2),
            ReplacementTransform(panah2.copy(), jawaban1_14)
        )
        self.play(
            Write(panah3),
            ReplacementTransform(panah3.copy(), jawaban1_15)
        )

        jawaban1_16 = TextMobject("Jadi vektor eigen dari A yang bersesuaian dengan $\lambda$ \\\\ adalah vektor tak nol:")
        jawaban1_17 = TextMobject("x")
        samadengan = TextMobject("=")
        jawaban1_18 = TexMobject(r"\begin{bmatrix} -2s \\ s \end{bmatrix}")
        jawaban1_19 = TexMobject(r"s\begin{bmatrix} -2 \\ 1 \end{bmatrix}")
        jawaban1_20 = TextMobject("Maka untuk $\lambda =2$, basisnya adalah:")
        jawaban1_21 = TexMobject(r"\begin{bmatrix} -2 \\ 1 \end{bmatrix}")

        jawaban1_16.next_to(soal1, DOWN)
        samadengan.next_to(jawaban1_16, 3*DOWN)
        jawaban1_17.next_to(samadengan, LEFT)
        jawaban1_18.next_to(samadengan, RIGHT)
        jawaban1_19.next_to(samadengan, RIGHT)
        jawaban1_20.next_to(samadengan, 3*DOWN)
        jawaban1_21.next_to(jawaban1_20, DOWN)

        self.play(
            ReplacementTransform(jawaban1_10, jawaban1_16),
            ReplacementTransform(jawaban1_11, jawaban1_17),
            ReplacementTransform(jawaban1_11.copy(), samadengan),
            ReplacementTransform(jawaban1_11.copy(), jawaban1_18),
            FadeOut(jawaban1_12),
            FadeOut(jawaban1_13),
            FadeOut(jawaban1_14),
            FadeOut(jawaban1_15),
            FadeOut(panah2),
            FadeOut(panah3)
        )
        self.play(ReplacementTransform(jawaban1_18, jawaban1_19))
        self.play(ReplacementTransform(samadengan.copy(), jawaban1_20))
        self.play(ReplacementTransform(jawaban1_20.copy(), jawaban1_21))

        soal2_1 = TextMobject("2. Tentukan eigenvalues dan eigenvectors dari matriks")
        soal2_2 = TexMobject(r"A=\begin{bmatrix} 3 & 1 & 1 \\ 2 & 4 & 2 \\ 1 & 1 & 3 \end{bmatrix}")
        jawaban2_1 = TextMobject("Dengan menggunakan persamaan karakteristik: det(A-$\lambda$I)=0")
        jawaban2_2 = TexMobject(r"\begin{bmatrix} 3-\lambda  & 1 & 1 \\ 2 & 4-\lambda  & 2 \\ 1 & 1 & 3-\lambda  \end{bmatrix}=0")
        jawaban2_3 = TexMobject(r"{ \left( 3-\lambda  \right)  }^{ 2 }\left( 4-\lambda  \right) +2+2-\left( 4-\lambda  \right) -2\left( 3-\lambda  \right) -2\left( 3-\lambda  \right) =0")
        jawaban2_4 = TexMobject(r"\left( 3-\lambda  \right) \left[ \left( 3-\lambda  \right) \left( 4-\lambda  \right) -4 \right] +\lambda =0")
        jawaban2_5 = TexMobject(r"\left( 3-\lambda  \right) \left( 8-7\lambda +{ \lambda  }^{ 2 } \right) +\lambda =0")

        soal2_1.next_to(judul, 2*DOWN)
        soal2_2.next_to(soal2_1, DOWN)
        jawaban2_1.next_to(soal2_2, DOWN)
        jawaban2_2.next_to(jawaban2_1, DOWN)
        jawaban2_3.next_to(jawaban2_1, DOWN)
        jawaban2_4.next_to(jawaban2_3, DOWN)
        jawaban2_5.next_to(jawaban2_4, DOWN)

        self.play(
            FadeOut(jawaban1_16),
            FadeOut(jawaban1_17),
            FadeOut(jawaban1_19),
            FadeOut(jawaban1_20),
            FadeOut(jawaban1_21),
            FadeOut(samadengan),
            ReplacementTransform(soal1, soal2_1),
            Write(soal2_2)
        )
        self.wait(2)
        self.play(
            FadeIn(jawaban2_1),
            Write(jawaban2_2)
        )
        self.play(ReplacementTransform(jawaban2_2, jawaban2_3))
        self.play(ReplacementTransform(jawaban2_3.copy(), jawaban2_4))
        self.play(ReplacementTransform(jawaban2_4.copy(), jawaban2_5))
        self.wait(2)
        self.play(
            FadeOut(soal2_1),
            FadeOut(soal2_2),
            FadeOut(jawaban2_1),
            FadeOut(jawaban2_3),
            FadeOut(jawaban2_4),
            FadeOut(jawaban2_5)
        )
#lanjutan jawaban no.2
class tambahan(Scene):
    def construct(self):
        textnn = TextMobject("Dari persamaan diatas didapat")
        jawaban2_9 = TextMobject("${\lambda}_{1}$ =2, ${\lambda}_{2}$ = 6")
        jawaban2_10 = TextMobject("Ruang vektor:")
        jawaban2_11 = TexMobject(r"\begin{bmatrix} 3-\lambda  & 1 & 1 \\ 2 & 4-\lambda  & 2 \\ 1 & 1 & 3-\lambda  \end{bmatrix}=\begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix}")
        jawaban2_12 = TextMobject("Untuk ${\lambda}_{1}=2$ diperoleh:")
        jawaban2_13 = TexMobject(r"\begin{bmatrix} 1 & 1 & 1 \\ 2 & 2 & 2 \\ 1 & 1 & 1 \end{bmatrix} \begin{bmatrix} { x }_{ 1 } \\ { x }_{ 2 } \\ { x }_{ 3 } \end{bmatrix} =  \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix}")
        panah2 = Arrow(LEFT).scale(1)
        jawaban2_14 = TextMobject("${x}_{1}+{x}_{2}+{x}_{3}=0$ \\\\ ${2x}_{1}+{2x}_{2}+{2x}_{3}=0$ \\\\ ${x}_{1}+{x}_{2}+{x}_{3}=0$")
        jawaban2_16 = TextMobject("Jadi vektor eigen dari A yang bersesuaian dengan $\lambda$ \\\\ adalah vektor tak nol:")
        jawaban2_17 = TextMobject("x")
        samadengan1 = TextMobject("=")
        jawaban2_18 = TexMobject(r"\begin{bmatrix} 0s \\ 0s \\ 0s \end{bmatrix}")
        jawaban2_19 = TexMobject(r"s\begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix}")
        jawaban2_20 = TextMobject("Maka untuk $\lambda =2$, basisnya adalah:")
        jawaban2_21 = TexMobject(r"\begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix}")
        
        
        jawaban3_12 = TextMobject("Untuk ${\lambda}_{2}=6$ diperoleh:")
        jawaban3_13 = TexMobject(r"\begin{bmatrix} -3 & 1 & 1 \\ 2 & -2 & 2 \\ 1 & 1 & -3 \end{bmatrix}\begin{bmatrix} { x }_{ 1 } \\ { x }_{ 2 } \\ { x }_{ 3 } \end{bmatrix}=\begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix}")
        panah4 = Arrow(LEFT).scale(1)
        jawaban3_14 = TextMobject("${-3x}_{1}+{x}_{2}+{x}_{3}=0$ \\\\ ${2x}_{1}-{2x}_{2}+{2x}_{3}=0$ \\\\ ${x}_{1}+{x}_{2}-{3x}_{3}=0$")
        panah5 = Arrow(UP).scale(1)
        jawaban3_15a = TextMobject("${x}_{1}=8/7{x}_{2}$")
        jawaban3_15b = TextMobject("${x}_{3}=5/7{x}_{2}$")
        jawaban3_16 = TextMobject("Jadi vektor eigen dari A yang bersesuaian dengan $\lambda$ \\\\ adalah vektor tak nol:")
        jawaban3_17 = TextMobject("x")
        samadengan2 = TextMobject("=")
        jawaban3_18 = TexMobject(r"\begin{bmatrix} {8/7}s \\ s \\ {5/7}s \end{bmatrix}")
        jawaban3_19 = TexMobject(r"s\begin{bmatrix} 8/7 \\ 1 \\ 5/7 \end{bmatrix}")
        jawaban3_20 = TextMobject("Maka untuk $\lambda =6$, basisnya adalah:")
        jawaban3_21 = TexMobject(r"\begin{bmatrix} 8/7 \\ 1 \\ 5/7 \end{bmatrix}")
        
        
        textnn.to_edge(UP, buff=1)
        jawaban2_9.next_to(jawaban2_11,DOWN)
        jawaban2_12.next_to(textnn, DOWN)
        jawaban2_10.next_to(textnn, 6*DOWN + 0.5*LEFT)
        jawaban2_11.next_to(jawaban2_10, RIGHT)
        jawaban2_13.next_to(jawaban2_12, DOWN + LEFT)
        jawaban2_13.shift(1.5*RIGHT)
        panah2.next_to(jawaban2_13, RIGHT)
        jawaban2_14.next_to(panah2, RIGHT)
        jawaban2_16.next_to(textnn, DOWN)
        samadengan1.next_to(jawaban2_16, 4*DOWN)
        jawaban2_17.next_to(samadengan1, LEFT)
        jawaban2_18.next_to(samadengan1, RIGHT)
        jawaban2_19.next_to(samadengan1, RIGHT)
        jawaban2_20.next_to(samadengan1, 4*DOWN)
        jawaban2_21.next_to(jawaban2_20, DOWN)
        
        self.play(Write(textnn))
        self.play(FadeIn(jawaban2_9), 
                  FadeIn(jawaban2_10), 
                  FadeIn(jawaban2_11))
        self.wait(3)
        self.remove(textnn, jawaban2_9, jawaban2_10, jawaban2_11)
        self.play(Write(jawaban2_12), Write(jawaban2_13), Write(panah2), Write(jawaban2_14))
        self.wait(2)
        self.remove(jawaban2_13, panah2, jawaban2_14)
        self.play(Transform(jawaban2_12, jawaban2_16))
        self.play(Write(jawaban2_17), Write(samadengan1), Write(jawaban2_18))
        self.wait(2)
        self.play(Transform(jawaban2_18, jawaban2_19))
        self.wait(2)
        self.play(ReplacementTransform(jawaban2_18.copy(), jawaban2_20),
                  ReplacementTransform(samadengan1.copy(), jawaban2_21)
                  )
        self.wait(3)
        self.play(FadeOut(jawaban2_12),
                  FadeOut(jawaban2_17),
                  FadeOut(samadengan1),
                  FadeOut(jawaban2_18),
                  FadeOut(jawaban2_20),
                  FadeOut(jawaban2_21))
        self.wait(2)
                
        
        jawaban3_12.next_to(textnn, DOWN) 
        jawaban3_13.next_to(jawaban3_12, DOWN + LEFT)
        jawaban3_13.shift(2 * RIGHT)
        panah4.next_to(jawaban3_13, RIGHT)
        jawaban3_14.next_to(panah4, RIGHT)
        panah5.next_to(jawaban3_14, DOWN)
        jawaban3_15a.next_to(panah5, DOWN)
        jawaban3_15b.next_to(jawaban3_15a, DOWN)
        jawaban3_16.next_to(textnn, DOWN)
        samadengan2.next_to(jawaban3_16, 4*DOWN)
        jawaban3_17.next_to(samadengan2, LEFT)
        jawaban3_18.next_to(samadengan2, RIGHT)
        jawaban3_19.next_to(samadengan2, RIGHT)
        jawaban3_20.next_to(samadengan2, 4*DOWN)
        jawaban3_21.next_to(jawaban3_20, DOWN)
        
        self.play(Write(jawaban3_12),
                  Write(panah4),
                  Write(jawaban3_13),
                  Write(jawaban3_14),
                  Write(panah5),
                  Write(jawaban3_15a),
                  Write(jawaban3_15b))
        self.wait(2)
        self.play(FadeOut(panah4),
                  FadeOut(jawaban3_13),
                  FadeOut(jawaban3_14),
                  FadeOut(panah5),
                  FadeOut(jawaban3_15a),
                  FadeOut(jawaban3_15b))
        self.play(ReplacementTransform(jawaban3_12, jawaban3_16))
        self.play(Write(jawaban3_17),
                  Write(samadengan2),
                  Write(jawaban3_18))
        self.wait(2)
        self.play(ReplacementTransform(jawaban3_18, jawaban3_19))
        self.play(ReplacementTransform(jawaban3_18.copy(), jawaban3_20),
                  ReplacementTransform(samadengan2.copy(), jawaban3_21)
                  )
        self.wait(3)
        self.play(FadeOut(jawaban3_16),
                  FadeOut(jawaban3_17),
                  FadeOut(samadengan2),
                  FadeOut(jawaban3_19),
                  FadeOut(jawaban3_20),
                  FadeOut(jawaban3_21))
        self.wait(3)
    
    
#Check Player        
if __name__== '__main__':
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"python -m manim {script_name} {SCENE} {FLAGS}")

    #DEBUGGER CREDITS
    
    # M. Ali Syaifudin from ITB - Astronomy '16
    # M. Taufiqurrahman from UGM - Electronic and Instrumentation '14
