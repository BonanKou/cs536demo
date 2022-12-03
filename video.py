from tkinter import font
from turtle import circle
from manimlib import *
from manim_fonts import *

big = 60
middle = 40
small = 25

time_say_hi = 3
class TextExample(Scene):
    CONFIG = {
      "camera_config": {"background_color": "#000000"},
    }
    def construct(self):
        # #####################################################################################
        # Today I’m going to present our reproduction of pHPA: A Proactive Autoscaling Framework for Microservice Chain. I bet many of you know what a microservice is but I would like to briefly introduce the concept of a microservice for those who do not.
        #####################################################################################
        # text = Text("Reproducing...\npHPA: A Proactive Autoscaling Framework\nfor Microservice Chain", font="Source Han Sans ExtraLight", 
        # font_size=big, 
        # )

        # RegisterFont("Source Sans Pro")
        # text = Text("Reproducing\n", font='Source Sans Pro ExtraLight', stroke_width=0, t2g={'pHPA: A Proactive Autoscaling Framework\nfor Microservice Chain':(BLUE, GREEN)})
        # self.play(Write(text))
        # text2 = Text("pHPA: A Proactive Autoscaling Framework\nfor Microservice Chain", font='Source Sans Pro ExtraLight')
        # text2.set_color_by_gradient(BLUE, GREEN)
        # difference = Text(
        #     """
        #     Bonan Kou, Yuan Tian, Zhaoqing Wu, Chengfei Wu, Hao Shen
        #     """,
        #     font='Source Sans Pro ExtraLight', font_size=small,
        #     # t2c is a dict that you can choose color for different text
        #     # t2c={"Text": BLUE, "TexText": BLUE, "LaTeX": ORANGE}
        # )
        with RegisterFont("Source Sans Pro") as fonts:
          the_font = "Source Sans Pro ExtraLight"
          # text1 = Text("A Reproduction Of", font=the_font)
          # text = Text("pHPA: A Proactive Autoscaling Framework\nfor Microservice Chain [SigConf 22]", font=the_font, t2s={"[SigConf 22]": ITALIC})
          # print(fonts)
          # text.set_color_by_gradient(BLUE, PURPLE, GREEN)
          # texts = VGroup(text1, text).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
          # # VGroup(text, difference).arrange(DOWN, buff=1)

          # difference = Text(
          #     """
          #     Bonan Kou / Yuan Tian / Zhaoqing Wu / Chengfei Wu / Hao Shen
          #     """,
          #     font='Source Sans Pro ExtraLight', font_size=27,
          #     # t2c is a dict that you can choose color fo different text
          #     # t2c={"Text": BLUE, "TexText": BLUE, "LaTeX": ORANGE}
          # )
          # VGroup(texts, difference).arrange(DOWN, buff=1)
          # self.play(Write(text1), run_time=0.5)
          # self.play(Write(text))
          # self.add(difference)
          # self.wait(time_say_hi)
          # self.remove(VGroup(texts, difference))

          
          # self.play(FadeOut(text), FadeOut(difference, shift=DOWN))

          #####################################################################################
          # 1.	Suppose you have a single program that carries out some basic logic.
          #####################################################################################
          section = Text("1. Microservice", font=the_font, font_size=30).move_to([-6, 3.5, 0], aligned_edge=LEFT)
          self.add(section)
          # square = SVGMobject("cloud.svg", stroke_width = 0, opacity=0.7).scale(0.7)
          # image = SVGMobject("cube.svg", stroke_width = 0).scale(0.2)
          # image.move_to([0, -0.1, 0])

          # self.play(FadeIn(square), FadeIn(image))
          # services = [image]
          # def spawn(distance):
          #   image2 = SVGMobject("cube.svg", stroke_width = 0).scale(0.2)
          #   fade_list = []
          #   play_list = []
          #   patch_fade = []
          #   patch_list = []
          #   for i in [0, distance, -distance]:
          #     for j in [0, distance, -distance]:
          #       if (i != 0 or j != 0) and not (abs(i) == 1 and abs(j) == 1):
          #         image2 = SVGMobject("cube.svg", stroke_width = 0).scale(0.2)
          #         image2.move_to([0, -0.1, 0])
          #         services.append(image2)
          #         if abs(distance) == 1.0:
          #           image2.move_to([i / 2, j / 2 - 0.1, 0])
          #         fade_list.append(FadeIn(image2))
          #         play_list.append(image2.animate.move_to([i, j - 0.1, 0]))

          #         if (i == 0 or j == 0) and abs(distance) == 1.0:
          #           image3 = SVGMobject("cube.svg", stroke_width = 0).scale(0.2)
          #           image4 = SVGMobject("cube.svg", stroke_width = 0).scale(0.2)
          #           services.append(image3)
          #           services.append(image4)
          #           image3.move_to([i, j- 0.1, 0])
          #           image4.move_to([i, j- 0.1, 0])
          #           patch_fade.append(FadeIn(image3))
          #           patch_fade.append(FadeIn(image4))
          #           if i == 0:
          #             patch_list.append(image3.animate.move_to([i - 0.5, j - 0.1, 0]))
          #             patch_list.append(image4.animate.move_to([i + 0.5, j - 0.1, 0]))
          #           else:
          #             patch_list.append(image3.animate.move_to([i, j - 0.5 - 0.1, 0]))
          #             patch_list.append(image4.animate.move_to([i, j + 0.5 - 0.1, 0]))

          #   # self.play(*fade_list)
          #   self.play(*play_list, square.animate.scale(1.7, about_point=[0, -0.1, 0]), run_time=0.7)
          #   # self.play()
          #   self.play(*patch_list, run_time=0.7)

          # ########################################################################################
          # # As more and more functionalities are added, this program becomes too complicated to debug and scale.
          # #####################################################################################
          # spawn(0.5)
          # spawn(1.0)
          # # self.play()
          # for i in range(1):
          #   color_list = []
          #   self.play(*color_list, square.animate.set_color("#f0d23e"), run_time=0.5)
          #   self.play(*color_list, square.animate.set_color("#ff574d"), run_time=1)


          # monolith = VGroup(square, *services)
          # self.play(FadeOut(monolith, LEFT))


          # user.add_updater(lambda mob, dt: mob.rotate(-1*DEGREES))
          # user.add_updater(lambda mob, dt: mob.shift([.1,0.,0]))
          def split(x, y):
            new_square = SVGMobject("cloud.svg", stroke_width = 0, opacity=0.7).scale(0.7 * 1.7 * 1.7).scale(0.3, about_point=[0, -0.1, 0])
            new_image = SVGMobject("cube.svg", stroke_width = 0).move_to([0, -0.1, 0]).scale(0.25)
            m = VGroup(new_square, new_image).move_to([x, y, 0]).scale(0.7)
            # line = Arrow(user,m, buff=0)
            self.play(FadeIn(m),run_time=0.01)
            m.add_updater(lambda mob, dt: mob.rotate(-1*DEGREES, about_point=[x + 0.05, y + 0.05, 0]))
            m.add_updater(lambda mob, dt: mob.rotate(1*DEGREES))
            return m


          microservices = []
          for j in [2, 1, 0, -1, -2]:
            for i in [-4, -2, 0, 2, 4]:
              microservices.append(split(i, j))

          
          all_ms = VGroup(*microservices)
          # all_ms.rotate(-40*DEGREES, axis=UP)
          # self.wait(5)
          for i in microservices:
            i.clear_updaters()
          self.play(all_ms.animate.scale(2))

          for i in microservices:
            i.clear_updaters()
          
          fades = []
          enlarge = []
          for index, i in enumerate(microservices):
            if index == 12:
              fades.append(i.animate.move_to([-4, 0, 0], aligned_edge=LEFT))
              
            elif index == 13:
              fades.append(i.animate.move_to([4, 0, 0], aligned_edge=RIGHT))
              
            else:
              fades.append(FadeOut(i))
          self.play(*fades, run_time=0.5)


          now = self.time
          microservices[12].add_updater(lambda m: m.shift(math.cos(self.time - now) * 0.001 * UP))
          microservices[13].add_updater(lambda m: m.shift(math.cos(self.time - now + 1) * 0.001 * UP))

          enlarge.append(microservices[12].animate.scale(1.2))
          enlarge.append(microservices[13].animate.scale(1.2))

          self.play(*enlarge, run_time=0.5)


          # self.wait(1)
          # lines.clear_updaters()


          ############################################################
          # These components can be indenpendent developed and scaled
          ############################################################

          ################################################################
          # These microservices communicate via RPC, streaming, and message broker.
          cloud_height = (microservices[12].get_top()[1] - microservices[12].get_bottom()[1]) - 0.3
          cloud_width = (microservices[12].get_right()[0] - microservices[12].get_left()[0])
          distance = microservices[13].get_x() - microservices[12].get_x()
          user = SVGMobject("server.svg", stroke_width = 0, opacity=0.7).scale(0.7).move_to([0, 2, 0]).scale(0.4)
          m12_loc = microservices[12].get_center()
          m13_loc = microservices[13].get_center()
          a1 = Arrow(start=user, end=[m12_loc[0], m12_loc[1] - 0.1, m12_loc[2]], stroke_width = 3, color=BLUE)
          a2 = Arrow(start=user, end=[m13_loc[0], m13_loc[1] - 0.1, m13_loc[2]], stroke_width = 3, color=BLUE)
          line1 = Rectangle(height= cloud_height / 3, width=distance, color=WHITE, stroke_width=0)
          # line1.move_to([microservices[12].get_x(), microservices[12].get_top()[1], 0], aligned_edge=LEFT)
          line1.set_fill(["#764BA2", "#667EEA"], opacity=1)


          line2 = Rectangle(height= cloud_height / 3, width=distance, color=WHITE, stroke_width=0)
          # line2.move_to([microservices[12].get_x(), microservices[12].get_top()[1]- cloud_height / 3, 0], aligned_edge=LEFT)
          line2.set_fill(["#4E65FF", "#92EFFD", "#4E65FF"], opacity=1)

          line3 = Rectangle(height= cloud_height / 3, width=distance, color=WHITE, stroke_width=0)
          # line3.move_to([microservices[12].get_x(), microservices[12].get_top()[1]- 2* cloud_height / 3, 0], aligned_edge=LEFT)
          line3.set_fill(["#D4145A", "#FBB03B", "#D4145A"], opacity=1)

          lines = VGroup(line1, line2, line3).arrange(DOWN, buff=0).move_to([0 - distance / 2,0,0], aligned_edge=LEFT)

          # self.bring_to_back(line2)
          # self.bring_to_back(line3)
          self.wait(0.3)
          self.add(lines)
          self.add(microservices[12])
          self.add(microservices[13])
          # lines.stretch_to_fit_width(distance)
          # self.play(lines.animate.stretch_to_fit_width(distance))
          # self.bring_to_back(lines)
          

          text1 = Text("Remote procedure call (RPC)", font=the_font,font_size=27, color="#f5f5f5").move_to(line1)
          text2 = Text("Streaming", font=the_font,font_size=27, color="#f5f5f5").move_to(line2)
          text3 = Text("Message broker", font=the_font,font_size=27, color="#f5f5f5").move_to(line3)

          lines.set_width(0.1, stretch=True)
          self.play(lines.animate.set_width(distance, stretch=True), run_time=0.5)




          text1.set_color_by_gradient("#bdc9fc", "#FFFFFF", "#bdc9fc")
          text2.set_color_by_gradient("#e6e3e3", "#92EFFD", "#e6e3e3")
          text3.set_color_by_gradient("#FBB03B", "#e6e3e3", "#FBB03B")
          self.add(text1)
          self.add(text2)
          self.add(text3)


          self.wait(3)



          self.remove(text1)
          self.remove(text2)
          self.remove(text3)
          self.play(lines.animate.set_width(0.01, stretch=True), run_time=0.5)
          self.remove(lines)



          self.add(user)
          self.play(microservices[12].animate.shift(DOWN*1), microservices[13].animate.shift(DOWN*1), ShowCreation(a1), ShowCreation(a2))
          self.wait(2)
          self.play(Uncreate(a1), Uncreate(a2), FadeOut(user))

          self.play(microservices[12].animate.shift(UP*1), microservices[13].animate.shift(UP*1))




          self.play(microservices[12].animate.scale(3 / 2), run_time=0.5)
          self.play(microservices[12].animate.scale(2/ 3), run_time=0.5)
          self.play(microservices[13].animate.scale(3 / 2), run_time=0.5)
          self.play(microservices[13].animate.scale(2/ 3), run_time=0.5)


          # lines.add_updater(lambda m: m.set_width((self.time - now) * distance, stretch=True))
          # self.wait(1)
          # lines.clear_updaters()

          # self.add(line2)
          # self.add(line3)


          # # line1 = Line([microservices[12].get_x(), 0, 0], [microservices[13].get_x(), 0, 0], color = PURPLE, buff=0, stroke_width=7)


          # combo1 = VGroup(text1, line1).arrange(DOWN, buff=0.1).shift([0, 0.45, 0])

          # text2 = Text("Streaming", font_size=30, font=the_font)
          # line2 = Line([microservices[12].get_x(), 0, 0], [microservices[13].get_x(), 0, 0], color = ORANGE, buff=0, stroke_width=7)
          # combo2 = VGroup(text2, line2).arrange(DOWN, buff=0.1).shift([0, -0.15, 0])
          # text3 = Text("Message broker", font_size=30, font=the_font)
          # line3 = Line([microservices[12].get_x(), 0, 0], [microservices[13].get_x(), 0, 0], color = GREEN, buff=0, stroke_width=7).shift([0, -0.75, 0])
          # combo3 = VGroup(text3, line3).arrange(DOWN, buff=0.1).shift([0, -0.75, 0])

          # self.bring_to_back(line1)
          # self.bring_to_back(line2)
          # self.bring_to_back(line3)
          # # line2 = Arrow(microservices[13], microservices[12], buff=0)
          # # line3 = Arrow(microservices[12], microservices[13], buff=0)

          # self.play(ShowCreation(line1), Write(text1), ShowCreation(line2), Write(text2), Write(text3), ShowCreation(line3))

          # # self.play(*enlarge, run_time=0.5)
          # # m = split(2, -2)
          # # split(-2, -1)
          # # split(2, 2)
          # # split(2.5, 0)
          # # split(-1.5, 2)

          # This flexibility brings a lot...
          cascading_effect = Text("Cascading Effect", font_size=big, font=the_font).move_to([20, 0, 0])
          left = VGroup(microservices[12], microservices[13])

          # self.play(Uncreate(line1), FadeOut(text1), Uncreate(line2), FadeOut(text2), FadeOut(text3), Uncreate(line3))

          self.remove(text1)
          self.remove(text2)
          self.remove(text3)

          def shift(prev, next = None, wait=1):
            if next != None:
              self.play(prev.animate.move_to([-20, 0, 0]), next.animate.move_to([0, 0, 0]), run_time=wait)
            else:
              self.play(prev.animate.move_to([-20, 0, 0]))
            self.remove(prev)

          shift(VGroup(microservices[12], microservices[13]))

          self.remove(section)
          section = Text("2. Cascading effect", font=the_font, font_size=30).move_to([-6, 3.5, 0], aligned_edge=LEFT)
          self.add(section)
          while True:
            self.wait(10)
        
TextExample().construct()