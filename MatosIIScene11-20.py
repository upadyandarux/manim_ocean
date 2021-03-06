# This code was made by M. Ridho Novrian
# With a lil bit of change from Dhimas Upadyandaru

from big_ol_pile_of_manim_imports import *
#from manimlib.imports import *
from objectPosition import *
import os
import pyclbr
import numpy as np


      
from big_ol_pile_of_manim_imports import *

 
class Scene1(Scene):
    def construct(self):
       #grid = NumberPlane()
       #grid.add_coordinates()
       firsttext=TextMobject(r"Persamaan \: Difusi",color=RED_B)
       firsttext.to_edge(LEFT)
       thirdtext=TextMobject("Persamaan","Difusi").scale(1.75)
       thirdtext[0].set_color(BLUE)
       thirdtext[1].set_color(YELLOW)
       thirdtext.to_edge(UP)
       r = TexMobject(r" \triangledown^{2}u = \frac{1}{\alpha ^{2}}\frac{\partial u}{\partial t}....(1)} ",color=TEAL).scale(1.3)
       r.set_submobject_colors_by_gradient(BLUE,YELLOW)
       r1= TexMobject(r" \triangledown^{2}u = \frac{1}{\alpha ^{2}}\frac{\partial u}{\partial t}....(1)} ",color=TEAL).scale(1.3)
       r1.to_edge(UP)
       r1.set_submobject_colors_by_gradient(RED,GREEN)
       vector1 = Arrow(np.array([-0.2,2,0]),np.array([3,1,0]),buff=0,tip_length=0.4,width=1,color=RED_B)
       vector2 = Arrow(np.array([-2,2.2,0]),np.array([-3.2,1,0]),buff=0,tip_length=0.4,width=1,color=RED_B)
       v1=TextMobject("Karakteristik Medium").scale(1)
       v1.move_to(3*RIGHT)
       v2=TextMobject("Fungsi Skalar(r,t)").scale(1.2)
       v2.move_to(3*LEFT)
       v3=TextMobject("U(r,t)").scale(1.5)
       v3.move_to(3*RIGHT)
       ket = TextMobject("r = variabel ruang",color=YELLOW).scale(1)
       ket.move_to(1*DOWN)
       ket1 = TextMobject("t = variabel waktu",color=YELLOW).scale(1)
       ket1.move_to(1.5*DOWN)
       gabung = VGroup(ket,ket1,v1,v2,v3,vector1,vector2,r)
       
       #self.play(Write(grid),run_time=2)
       #self.wait()
       self.play(Write(firsttext))
       self.wait(3)
       self.play(Write(r),Transform(firsttext,thirdtext))
       self.wait(4)
       self.play(Uncreate(firsttext),run_time=2)
       self.wait()
       self.play(Transform(r,r1),run_time=2)
       self.wait()
       self.play(Write(vector1),Write(vector2))
       self.wait(2)
       self.play(FadeIn(v1),FadeIn(v2))
       self.wait(3)
       self.play(Transform(v1,v3))
       self.wait(2)
       self.play(Write(ket),Write(ket1))
       self.wait(3)
       self.play(Uncreate(gabung))
       self.wait(2)
       
class Scene2(Scene):
    def construct(self):
       par1 = TextMobject(r"Penyelesaian persamaan difusi", r" juga menggunakan metode pemisahan variabel sebagaimana yang telah dijelaskan sebelumnya. Untuk menyelesaikannya,", r" diasumsikan solusi yang berbentuk:",font="Arial" ).scale(0.8)       
       par1[0].set_color(BLUE)
       par1[2].set_color(BLUE)
       par1.move_to(2*UP) 
       rumus = TexMobject(r" u = ",r"F(x,y,z)",r"T(t) ").scale(1.2)
       rumus.set_submobject_colors_by_gradient(PINK,WHITE)
       rumus.move_to(0.5*DOWN)
       Br = Brace(rumus[1],DOWN,color=YELLOW)
       Tr = Br.get_text("Variabel Ruang")
       Tr.set_submobject_colors_by_gradient(ORANGE,YELLOW)
       Br1= Brace(rumus[2],UP,color=ORANGE)
       Tr1= Br1.get_text("Variabel Waktu")
       Tr1.set_submobject_colors_by_gradient(YELLOW,ORANGE)
       Formula= VGroup(Br,Tr,Br1,Tr1)
      
       
       
       self.play(Write(par1),run_time=6)
       self.wait(3)
       self.play(FadeIn(rumus),run_time=3)
       self.wait(4)
       self.play(ShowCreation(Formula),run_time=3)
       self.wait(4)
       self.play(Uncreate(Formula),Uncreate(rumus),Uncreate(par1))
       self.wait(2)
       
class Scene3(Scene):
    def construct(self):   
       rumus = TexMobject(r" u = ",r"F(x,y,z)",r"T(t) ").scale(1.2)
       rumus.set_submobject_colors_by_gradient(PINK,WHITE)   
       rumus.to_edge(UP)
       kata = TextMobject("Subtitusikan ke Persamaan (1)",font="ARIAL")
       kata.move_to(1.5*UP)
       r = TexMobject(r" \triangledown^{2}u", r"=", r"\frac{1}{\alpha ^{2}}",r"\frac{\partial u}{\partial t}....(1)} ").scale(1.3)
       r[0].set_color(PINK) 
       r[1].set_color(TEAL)
       r[2].set_color(RED)
       r[3].set_color(YELLOW)
       rumus1 = TexMobject(r"T\triangledown^{2}F=\frac{1}{\alpha^{2}}F\frac{\mathrm{d} T}{\mathrm{d} t}....(2)")
       rumus1.set_submobject_colors_by_gradient(RED,YELLOW,ORANGE)  
       kata2 = TextMobject("Maka Persamaannya menjadi:",font="ARIAL")
       kata2.move_to(1.5*UP)
       rumus3 = TexMobject(r"T\triangledown^{2}F=\frac{1}{\alpha^{2}}F\frac{\mathrm{d} T}{\mathrm{d} t}....(2)")
       rumus3.set_submobject_colors_by_gradient(RED,YELLOW,ORANGE)  
       rumus3.move_to(4.3*LEFT)
       kata3 = TextMobject("Maka Persamaannya menjadi:",font="ARIAL").scale(0.8)
       kata3.move_to((1.5*UP)+(4*LEFT))
       rumus4 = TexMobject(r" u = ",r"F(x,y,z)",r"T(t) ")
       rumus4.set_submobject_colors_by_gradient(PINK,WHITE)
       rumus4.to_corner(UP+LEFT)
       kata4 = TexMobject(r"kemudian\, kalikan \, dengan", r"\frac{1}{FT}.",font="ARIAL").scale(0.8)
       kata4[1].set_color(RED)
       kata4.to_corner(RIGHT+UP)
       kata5 = TextMobject("Menjadi:",font="ARIAL").scale(0.8)
       kata5.move_to((1.5*UP)+(4*RIGHT))
       rumus2 = TexMobject(r"\frac{1}{F}\triangledown^{2}F=\frac{1}{\alpha^{2}}\frac{1}{T}\frac{\mathrm{d} T}{\mathrm{d} t}....(3)")
       rumus2.set_submobject_colors_by_gradient(RED,WHITE,BLUE) 
       rumus2.to_edge(RIGHT)
       
       
       self.play(ShowCreation(rumus),run_time=3)
       self.wait(2)
       self.play(FadeIn(kata),ShowCreation(r),run_time=3)
       self.wait(2)
       self.play(Transform(kata,kata2),Transform(r,rumus1),run_time=3)
       self.wait(3)
       self.play(Transform(rumus,rumus4),Transform(kata,kata3),Transform(r,rumus3),run_time=2)
       self.wait(2)
       self.play(ShowCreation(kata4),run_time=2)
       self.wait(1)
       self.play(ShowCreation(kata5),run_time=2)
       self.wait(2)
       self.play(Write(rumus2),run_time=2)
       self.wait(3)
       self.play(Uncreate(rumus2),Uncreate(kata5),Uncreate(kata4),Uncreate(r),Uncreate(rumus),Uncreate(kata))
       self.wait(2)


class Scene4(Scene):
    def construct(self): 
       r1 = TexMobject(r" \triangledown^{2}u", r"=", r"\frac{1}{\alpha ^{2}}",r"\frac{\partial u}{\partial t}....(1)} ").scale(0.85)
       r1[0].set_color(PINK) 
       r1[1].set_color(TEAL) 
       r1[2].set_color(RED) 
       r1[3].set_color(YELLOW)
       r1.to_corner(UL).buff=0.5
       r2 = TexMobject(r"T",r"\triangledown^{2}",r"F",r"=\frac{1}{\alpha^{2}}", r"F", r"\frac{\mathrm{d}T}{\mathrm{d}t}....(2)").scale(0.85)
       r2[0].set_color(PINK) 
       r2[1].set_color(TEAL) 
       r2[2].set_color(RED) 
       r2[3].set_color(YELLOW) 
       r2[4].set_color(PURPLE) 
       r2[5].set_color(BLUE)
       r2.next_to(r1,DOWN).buff=1
       r3 = TexMobject(r"\frac{1}{F}",r"\triangledown^{2}F=",r"\frac{1}{\alpha^{2}}",r"\frac{1}{T}",r"\frac{\mathrm{d}T}{\mathrm{d} t}....(3)").scale(0.85)
       r3[0].set_color(RED_B) 
       r3[1].set_color(TEAL) 
       r3[2].set_color(RED) 
       r3[3].set_color(YELLOW) 
       r3[4].set_color(ORANGE)
       r3.next_to(r2,DOWN).buff=1
       r13=VGroup(r1,r2,r3)
       panah = Arrow(np.array([-4,0,0]),np.array([-4,-1,0]),buff=0,tip_length=0.4,width=1,color=YELLOW)
       panah1 = Arrow(np.array([-6,0,0]),np.array([-6,-1,0]),buff=0,tip_length=0.4,width=1,color=YELLOW)
       kata= TextMobject("Variabel Ruang",font="ARIAL").scale(0.6)
       kata.move_to((6*LEFT)+(1.25*DOWN))
       kata1= TextMobject("Variabel Waktu",font="ARIAL").scale(0.6)
       kata1.next_to(kata,RIGHT)
       gabung=VGroup(panah,kata,panah1,kata1)
       r4 = TexMobject(r"\frac{1}{F}\triangledown^{2}F = -k^{2}")
       r4.set_submobject_colors_by_gradient(PINK,WHITE)
       r4.to_corner(UR)
       r5 = TexMobject(r"\triangledown^{2}F + k^{2}F=0")
       r5.set_submobject_colors_by_gradient(PINK,WHITE)
       r5.next_to(r4,DOWN)
       kata2 = TextMobject("dan",font="ARIAL").scale(0.6)
       kata2.next_to(r5,DOWN)
       r6 = TexMobject(r"\frac{1}{\alpha ^{2}}\frac{1}{T}\frac{\mathrm{d}T}{\mathrm{d}t}=-k^{2}")
       r6.set_submobject_colors_by_gradient(WHITE,BLUE)
       r6.next_to(kata2,DOWN)
       r7 = TexMobject(r"\frac{\mathrm{d}T}{\mathrm{d}t}=-k^{2}\alpha ^{2}T")
       r7.set_submobject_colors_by_gradient(WHITE,BLUE)
       r7.next_to(r6,DOWN)
       total=VGroup(r4,r5,r6,r7,kata2)
       br=Brace(total,LEFT)
       tr = br.get_text("Persamaan (4)")
       tr.set_color(YELLOW)
       total1=VGroup(tr,br,total,gabung)
      
       
       self.play(ShowCreation(r13),run_time=6)
       self.wait(3)
       self.play(Write(gabung),run_time=3)
       self.wait(2)
       self.play(Write(r4),run_time=3)
       self.wait(1)
       self.play(Write(r5),run_time=3)
       self.wait(1)
       self.play(Write(kata2),Write(r6),run_time=3)
       self.wait(2)
       self.play(Write(r7),run_time=3)
       self.wait(2)
       self.play(Write(br),Write(tr),run_time=4)
       self.wait(4)
       self.play(Uncreate(total1),Uncreate(r13))
       self.wait(2)
       
       
class Scene5(Scene):
    def construct(self):     
       r4 = TexMobject(r"\frac{1}{F}\triangledown^{2}F = -k^{2}")
       r4.set_submobject_colors_by_gradient(PINK,WHITE)
       r4.to_edge(UP+LEFT)
       r5 = TexMobject(r"\triangledown^{2}F + k^{2}F=0")
       r5.set_submobject_colors_by_gradient(PINK,WHITE)
       r5.next_to(r4,DOWN)
       kata = TextMobject("dan",font="ARIAL").scale(0.6)
       kata.next_to(r5,DOWN)
       r6 = TexMobject(r"\frac{1}{\alpha ^{2}}\frac{1}{T}\frac{\mathrm{d}T}{\mathrm{d}t}=-k^{2}")
       r6.set_submobject_colors_by_gradient(WHITE,BLUE)
       r6.next_to(kata,DOWN)
       r7 = TexMobject(r"\frac{\mathrm{d}T}{\mathrm{d}t}=-k^{2}\alpha ^{2}T")
       r7.set_submobject_colors_by_gradient(WHITE,BLUE)
       r7.next_to(r6,DOWN)  
       r47=VGroup(r4,r5,r6,r7,kata)
       br=Brace(r47,RIGHT)
       tr = br.get_text("Persamaan (4)")
       tr.set_color(YELLOW)
       bt=VGroup(tr,br)
       r8 = TexMobject(r"T(t)=",r"A",r"e^{-k^{2}\alpha ^{2}t", r"}....(5)")
       r8[0].set_color(TEAL_B)
       r8[1].set_color(GREEN)
       r8[2].set_color(YELLOW)
       r8[3].set_color(BLUE)
       r8.to_edge(RIGHT)
       circle = Circle()
       circle.next_to(r8[1],0,buff=0).scale(0.25)
       kata1=TextMobject("A = Konstanta Integrasi",font="ARIAL")
       kata1.next_to(circle,2*DOWN)
       total = VGroup(r47,bt,r8,circle,kata1)
       
       rumus= TexMobject(r"\frac{\mathrm{d}^{2}F}{\mathrm{d}x^{2}}", r" + k^{2}F", r" = 0....(6)").scale(1.5)
       rumus[0].set_color(ORANGE)
       rumus[1].set_color(GREEN)
       rumus[2].set_color(PURPLE)
       rumus1= TexMobject(r"\frac{\mathrm{d}^{2}F}{\mathrm{d}x^{2}}", r" + k^{2}F", r" = 0....(6)").scale(1.5)
       rumus1[0].set_color(ORANGE)
       rumus1[1].set_color(GREEN)
       rumus1[2].set_color(PURPLE)
       rumus1.to_edge(UP)
       teks = TextMobject("yang solusinya adalah", font="ARIAL")
       teks.next_to(rumus1,DOWN,buff=1.75)
       rumus2= TexMobject(r"F(x)", r" = C\, cos\, kx ", r"+ D\, sin\, kx").scale(1.5)
       rumus2[0].set_color(ORANGE)
       rumus2[1].set_color(GREEN)
       rumus2[2].set_color(PURPLE)
       rumus2.next_to(teks,DOWN,buff=1.75)
       
       
       
       self.play(FadeIn(r47),run_time=4)
       self.wait(3)
       self.play(Write(bt),run_time=2)
       self.wait(2)
       self.play(Write(r8),run_time=3)
       self.wait(3)
       self.play(ShowCreation(circle),run_time=4)
       self.wait(2)
       self.play(Write(kata1),run_time=4)
       self.wait(2)
       self.play(Uncreate(total),run_time=3)
       self.wait(2)
       self.play(Write(rumus),run_time=4)
       self.wait(12)
       self.play(Transform(rumus,rumus1),run_time=2)
       self.wait(2)
       self.play(Write(teks))
       self.wait(2)
       self.play(Write(rumus2),run_time=2)
       self.wait(4)
       
       
       
