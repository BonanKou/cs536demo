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
        with RegisterFont("Source Sans Pro") as fonts:
          the_font = "Source Sans Pro ExtraLight"
          section = Text("1. Microservice", font=the_font, font_size=30).move_to([-6, 3.5, 0], aligned_edge=LEFT)

          # text1 = Text("A Reproduction Of", font=the_font)
          # text = Text("pHPA: A Proactive Autoscaling Framework\nfor Microservice Chain [APNet’21]", font=the_font, t2s={"APNet’21": ITALIC})
          # print(fonts)
          # text.set_color_by_gradient(BLUE, PURPLE, GREEN)
          # texts = VGroup(text1, text).arrange(DOWN, buff=0.1, aligned_edge=LEFT)

          # difference = Text(
          #     """
          #     Bonan Kou / Yuan Tian / Zhaoqing Wu / Chengfei Wu / Hao Shen
          #     """,
          #     font='Source Sans Pro ExtraLight', font_size=27,
          # )
          # VGroup(texts, difference).arrange(DOWN, buff=1)
          # self.play(Write(text1), run_time=0.5)
          # self.play(Write(text))
          # self.add(difference)
          # self.wait(time_say_hi)
          # self.remove(VGroup(texts, difference))
          

          # #####################################################################################
          # # 1.	Suppose you have a single program that carries out some basic logic.
          # #####################################################################################
          # self.add(section)
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

          #   self.play(*play_list, square.animate.scale(1.7, about_point=[0, -0.1, 0]), run_time=0.7)
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

          # def split(x, y):
          #   new_square = SVGMobject("cloud.svg", stroke_width = 0, opacity=0.7).scale(0.7 * 1.7 * 1.7).scale(0.3, about_point=[0, -0.1, 0])
          #   new_image = SVGMobject("cube.svg", stroke_width = 0).move_to([0, -0.1, 0]).scale(0.25)
          #   m = VGroup(new_square, new_image).move_to([x, y, 0]).scale(0.7)
          #   # line = Arrow(user,m, buff=0)
          #   self.play(FadeIn(m),run_time=0.01)
          #   m.add_updater(lambda mob, dt: mob.rotate(-1*DEGREES, about_point=[x + 0.05, y + 0.05, 0]))
          #   m.add_updater(lambda mob, dt: mob.rotate(1*DEGREES))
          #   return m


          # microservices = []
          # for j in [2, 1, 0, -1, -2]:
          #   for i in [-4, -2, 0, 2, 4]:
          #     microservices.append(split(i, j))

          
          # all_ms = VGroup(*microservices)

          # for i in microservices:
          #   i.clear_updaters()
          # self.play(all_ms.animate.scale(2))

          # for i in microservices:
          #   i.clear_updaters()
          
          # fades = []
          # enlarge = []
          # for index, i in enumerate(microservices):
          #   if index == 12:
          #     fades.append(i.animate.move_to([-4, 0, 0], aligned_edge=LEFT))
              
          #   elif index == 13:
          #     fades.append(i.animate.move_to([4, 0, 0], aligned_edge=RIGHT))
              
          #   else:
          #     fades.append(FadeOut(i))
          # self.play(*fades, run_time=0.5)


          # now = self.time
          # microservices[12].add_updater(lambda m: m.shift(math.cos(self.time - now) * 0.001 * UP))
          # microservices[13].add_updater(lambda m: m.shift(math.cos(self.time - now + 1) * 0.001 * UP))

          # enlarge.append(microservices[12].animate.scale(1.2))
          # enlarge.append(microservices[13].animate.scale(1.2))

          # self.play(*enlarge, run_time=0.5)

          # ############################################################
          # # These components can be indenpendent developed and scaled
          # ############################################################

          # ################################################################
          # # These microservices communicate via RPC, streaming, and message broker.
          # cloud_height = (microservices[12].get_top()[1] - microservices[12].get_bottom()[1]) - 0.3
          # cloud_width = (microservices[12].get_right()[0] - microservices[12].get_left()[0])
          # distance = microservices[13].get_x() - microservices[12].get_x()
          # user = SVGMobject("server.svg", stroke_width = 0, opacity=0.7).scale(0.7).move_to([0, 2, 0]).scale(0.4)
          # m12_loc = microservices[12].get_center()
          # m13_loc = microservices[13].get_center()
          # db1 = SVGMobject("database.svg", stroke_width = 0, opacity=0.7).scale(0.7).move_to([m12_loc[0], -2, 0]).scale(0.4)
          # db2 = SVGMobject("database.svg", stroke_width = 0, opacity=0.7).scale(0.7).move_to([m13_loc[0], -2, 0]).scale(0.4)

          # user_loc = user.get_center()
          # a1 = Arrow(start=user_loc, end=[m12_loc[0], m12_loc[1] - 0.1, m12_loc[2]], stroke_width = 3, color=BLUE)
          # a2 = Arrow(start=user_loc, end=[m13_loc[0], m13_loc[1] - 0.1, m13_loc[2]], stroke_width = 3, color=BLUE)

          # a3 = Arrow(start=[db2.get_center()[0], m12_loc[1]  + 0.9, m12_loc[2]], end=[db2.get_center()[0], db2.get_center()[1] + 0.1, db2.get_center()[2]], stroke_width = 3, color=BLUE)
          # a4 = Arrow(start=[db1.get_center()[0], m13_loc[1] + 0.9, m13_loc[2]], end=[db1.get_center()[0], db1.get_center()[1] + 0.1, db1.get_center()[2]], stroke_width = 3, color=BLUE)

          # line1 = Rectangle(height= cloud_height / 3, width=distance, color=WHITE, stroke_width=0)
          # line1.set_fill(["#764BA2", "#667EEA"], opacity=1)


          # line2 = Rectangle(height= cloud_height / 3, width=distance, color=WHITE, stroke_width=0)
          # line2.set_fill(["#4E65FF", "#92EFFD", "#4E65FF"], opacity=1)

          # line3 = Rectangle(height= cloud_height / 3, width=distance, color=WHITE, stroke_width=0)
          # line3.set_fill(["#D4145A", "#FBB03B", "#D4145A"], opacity=1)

          # lines = VGroup(line1, line2, line3).arrange(DOWN, buff=0).move_to([0 - distance / 2,0,0], aligned_edge=LEFT)

          # self.wait(0.3)
          # self.add(lines)
          # self.add(microservices[12])
          # self.add(microservices[13])

          # text1 = Text("Remote procedure call (RPC)", font=the_font,font_size=20, color="#f5f5f5").move_to(line1)
          # text2 = Text("Streaming", font=the_font,font_size=20, color="#f5f5f5").move_to(line2)
          # text3 = Text("Message broker", font=the_font,font_size=20, color="#f5f5f5").move_to(line3)

          # lines.set_width(0.1, stretch=True)
          # self.play(lines.animate.set_width(distance, stretch=True), run_time=0.5)

          # text1.set_color_by_gradient("#bdc9fc", "#FFFFFF", "#bdc9fc")
          # text2.set_color_by_gradient("#e6e3e3", "#92EFFD", "#e6e3e3")
          # text3.set_color_by_gradient("#FBB03B", "#e6e3e3", "#FBB03B")
          # self.add(text1)
          # self.add(text2)
          # self.add(text3)
          # self.wait(3)

          # self.remove(text1)
          # self.remove(text2)
          # self.remove(text3)
          # self.play(lines.animate.set_width(0.01, stretch=True), run_time=0.5)
          # self.remove(lines)

          # self.add(user)
          # self.bring_to_back(a1)
          # self.bring_to_back(a2)
          # self.play(microservices[12].animate.shift(DOWN*1), microservices[13].animate.shift(DOWN*1), ShowCreation(a1), ShowCreation(a2))
          # self.wait(2)
          # self.play(Uncreate(a1), Uncreate(a2), FadeOut(user))
          # self.bring_to_back(a1)
          # self.bring_to_back(a2)
          # self.play(microservices[12].animate.shift(UP*1), microservices[13].animate.shift(UP*1))


          # ########################################################################
          # # And have their own databse
          # self.bring_to_back(a3)
          # self.bring_to_back(a4)
          # self.add(db1)
          # self.add(db2)
          # self.play(microservices[12].animate.shift(UP*1), microservices[13].animate.shift(UP*1), ShowCreation(a3), ShowCreation(a4))


          # self.add(microservices[12])
          # self.add(microservices[13])

          # self.wait(3)
          # self.play(Uncreate(a3), Uncreate(a4), FadeOut(db1), FadeOut(db2))
          # self.play(microservices[12].animate.shift(DOWN*1), microservices[13].animate.shift(DOWN*1))
          
          # ########################################################################
          # self.play(microservices[12].animate.scale(3 / 2), run_time=0.5)
          # self.play(microservices[12].animate.scale(2 / 3), run_time=0.5)
          # self.play(microservices[13].animate.scale(3 / 2), run_time=0.5)
          # self.play(microservices[13].animate.scale(2 / 3), run_time=0.5)
        
          # # This flexibility brings a lot...
          # cascading_effect = Text("Cascading Effect", font_size=big, font=the_font).move_to([20, 0, 0])
          # left = VGroup(microservices[12], microservices[13])

          # self.remove(text1)
          # self.remove(text2)
          # self.remove(text3)

          # def shift(prev, next = None, wait=1):
          #   if next != None:
          #     self.play(prev.animate.move_to([-20, 0, 0]), next.animate.move_to([0, 0, 0]), run_time=wait)
          #   else:
          #     self.play(prev.animate.move_to([-20, 0, 0]))
          #   self.remove(prev)

          # shift(VGroup(microservices[12], microservices[13]))

          # self.remove(section)
          # section = Text("2. Cascading effect", font=the_font, font_size=30).move_to([-6, 3.5, 0], aligned_edge=LEFT)
          # self.add(section)


          # axes = Axes(
          #   # x-axis ranges from -1 to 10, with a default step size of 1
          #   x_range=(-1, 10),
          #   # y-axis ranges from -2 to 2 with a step size of 0.5
          #   y_range=(-2, 2, 0.5),
          #   # The axes will be stretched so as to match the specified
          #   # height and width
          #   height=3,
          #   width=4,
          #   # Axes is made of two NumberLine mobjects.  You can specify
          #   # their configuration with axis_config
          #   axis_config={
          #       "stroke_color": GREY_A,
          #       "stroke_width": 2,
          #   },
          #   # Alternatively, you can specify configuration for just one
          #   # of them, like this.
          #   y_axis_config={
          #       "include_tip": False,
          #   }
          # ).rotate(-90 * DEGREES, about_edge=IN)
          axes = NumberPlane(
            x_range=[0, 250, 25],
            y_range=[0, 3, 1],
            height = 2,
            width = 4,
            tips=False,
            faded_line_ratio = 1,
            axis_config={"include_numbers": False},
            # y_axis_config={"scaling": LogBase(custom_labels=True)},
          ).rotate(-90 * DEGREES, about_edge=IN)

          # axes.add_coordinate_labels(
          #     font_size=20,
          #     font = the_font,
          #     num_decimal_places=1,
          # )
          self.add(axes)
          while True:
            self.wait(10)
        
TextExample().construct()