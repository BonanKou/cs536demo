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

          # def split(x, y, scale=0.8):
          #   new_square = SVGMobject("cloud.svg", stroke_width = 0, opacity=0.8).scale(0.8 * 1.6 * 1.6).scale(0.3, about_point=[0, -0.1, 0])
          #   new_image = SVGMobject("cube.svg", stroke_width = 0).move_to([0, -0.1, 0]).scale(0.25)
          #   m = VGroup(new_square, new_image).move_to([x, y, 0]).scale(scale)
          #   # line = Arrow(user,m, buff=0)
          #   self.play(FadeIn(m),run_time=0.01)
          #   m.add_updater(lambda mob, dt: mob.rotate(-1*DEGREES, about_point=[x + 0.05, y + 0.05, 0]))
          #   m.add_updater(lambda mob, dt: mob.rotate(1*DEGREES))
          #   return m, new_square


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
          # square = SVGMobject("cloud.svg", stroke_width = 0, opacity=0.8).scale(0.8)
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

          #   self.play(*play_list, square.animate.scale(1.6, about_point=[0, -0.1, 0]), run_time=0.8)
          #   self.play(*patch_list, run_time=0.8)

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




          # microservices = []
          # for j in [2, 1, 0, -1, -2]:
          #   for i in [-4, -2, 0, 2, 4]:
          #     microservices.append(split(i, j)[0])

          
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
          # user = SVGMobject("server.svg", stroke_width = 0, opacity=0.8).scale(0.8).move_to([0, 2, 0]).scale(0.4)
          # m12_loc = microservices[12].get_center()
          # m13_loc = microservices[13].get_center()
          # db1 = SVGMobject("database.svg", stroke_width = 0, opacity=0.8).scale(0.8).move_to([m12_loc[0], -2, 0]).scale(0.4)
          # db2 = SVGMobject("database.svg", stroke_width = 0, opacity=0.8).scale(0.8).move_to([m13_loc[0], -2, 0]).scale(0.4)

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
  #         section = Text("2. Cascading effect", font=the_font, font_size=30).move_to([-6, 3.5, 0], aligned_edge=LEFT)
  #         self.add(section)

  #         ## The cascading effect #############################
  #         t1 = BulletedList("Microservices form complex dependency relationship", font=the_font, font_size=25).move_to([0, 0, 0])
  #         # t1 = BulletedList("Item 1", "Item 2", "Item 3", height=2, width=2)
  #         t2 = BulletedList("It takes 25 seconds (median) to create a new instance", font=the_font, font_size=25).move_to([0, 0, 0])
  #         t3 = BulletedList("These lags stack", font=the_font, font_size=25).move_to([0, 0, 0])
  #         t4 = BulletedList("Current autoscalers are slow", font=the_font, font_size=25)
  #         allts = VGroup(t1, t2, t3, t4).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        
  #         axes = NumberPlane(
  #           x_range=[0, 18, 1],
  #           y_range=[0, 3, 1],
  #           height = 3,
  #           width = 6,
  #           tips=False,
  #           faded_line_ratio = 4,
  #           # color= "#f5f5f5",
  #           color="#000000",
  #           axis_config={"include_numbers": False},
  #           # x_axis_config = {"include_ticks": True},
  #           background_line_style={
  #               "stroke_color": BLACK,
  #               "stroke_width": 2,
  #               "stroke_opacity": 0.6
  #           },
  #           faded_line_style={
  #             "stroke_color": BLACK,
  #           }
  #           # y_axis_config={"scaling": LogBase(custom_labels=True)},
  #         ).rotate(-90 * DEGREES, about_edge=IN).shift(LEFT*3)

  #         client = axes.get_graph(
  #           lambda x: 0.8,
  #           color="#B2BEB5",
  #           stroke_width=0.2,
  #           opacity=0.5,
  #         )
  #         # client = DashedVMobject(client)
  #         m1 = axes.get_graph(
  #           lambda x: 1.6,
  #           color="#B2BEB5",
  #           stroke_width = 0.2,
  #         )
  #         m2 = axes.get_graph(
  #           lambda x: 2.4,
  #           color="#B2BEB5",
  #           stroke_width = 0.2,
  #         )


  #         def traffic(thread, start, end, dimish_list, color = "#029ffa", width = 0.07, icon = True):
  #           box = Rectangle(height= 0.001, width=width, color=WHITE, stroke_width=0).move_to(axes.coords_to_point(start, thread), aligned_edge=UP)
  #           box.set_fill(color, opacity=1)
  #           height = axes.coords_to_point(start)[1] - axes.coords_to_point(end)[1]

  #           self.add(box)
  #           self.play(*dimish_list, box.animate.set_height(height, about_edge=UP, stretch=True), run_time=0.5)
  #           bl = SVGMobject("document.svg").scale(0.2).move_to(axes.coords_to_point((start + end) / 2, thread)).shift(RIGHT*0.25)
  #           # self.play(ShowCreation(traffic1))
  #           if icon:
  #             self.play(FadeIn(bl))
            
  #           if thread == 0.8:
  #             bar_list1.append(box)
  #           elif thread == 1.6:
  #             bar_list2.append(box)
  #             icon_list1.append(bl)
  #           else:
  #             bar_list3.append(box)
  #             icon_list2.append(bl)
  #           return box

  #         # self.play(ShowCreation(step_graph))
  #         # axes.add_coordinate_labels(
  #         #     font_size=20,
  #         #     font = the_font,
  #         #     num_decimal_places=1,
  #         # )


  #         def add_text(content, thread):
  #           client_t = Text(content, font=the_font, font_size=16).move_to(axes.coords_to_point(0, thread), aligned_edge=DOWN).shift(UP*0.13)
  #           self.add(client_t)
  #           return client_t

  #         label1 = add_text("Client", 0.8)
  #         label2 = add_text("Service 1", 1.6)
  #         label3 = add_text("Service 2", 2.4)


  #         self.play(FadeIn(axes))
  #         self.play(ShowCreation(m1), ShowCreation(m2), ShowCreation(client))
  #         self.add(allts)
  #         allts.next_to(axes).shift(RIGHT*1 + UP * 2)
  #         def diminish(bar_list, icon_list):
  #           animation_list = []
  #           for box in bar_list:
  #             box.generate_target()
  #             box.target.set_width(0.02, about_edge=UP, stretch=True)
  #             box.target.set_opacity(0.5)
  #             animation_list.append(MoveToTarget(box))
  #           for bl in icon_list:
  #             bl.generate_target()
  #             bl.target.set_opacity(0.5)
  #             bl.target.scale(0.8)
  #             animation_list.append(MoveToTarget(bl))
  #           return animation_list

  #         def survive(bar_list, icon_list):
  #           animation_list = []
  #           for box in bar_list:
  #             box.generate_target()
  #             box.target.set_width(0.07, about_edge=UP, stretch=True)
  #             box.target.set_opacity(1)
  #             animation_list.append(MoveToTarget(box))
  #           for bl in icon_list:
  #             bl.generate_target()
  #             bl.target.set_opacity(1)
  #             bl.target.scale(1.25)
  #             animation_list.append(MoveToTarget(bl))
  #           return animation_list

  #         def connect(start, end):
  #           dashed = DashedLine(start, end, color="#FFFFFF", stroke_width=0.5)
  #           dahsed_list.append(dashed)
  #           return [ShowCreation(dashed)]

  #         ########Traffic arrives
  #         bar_list1 = []
  #         bar_list2 = []
  #         bar_list3 = []
  #         icon_list1 = []
  #         icon_list2 = []
  #         dahsed_list = []
  #         traffic(0.8, 0, 3.1, [], "#12cc66", 0.1, False)
  #         temp = diminish(bar_list1, [])



  #         temp += connect(axes.coords_to_point(3.1, 0.8), axes.coords_to_point(3.1, 1.6))
  #         traffic(1.6, 3.1, 5.1, temp)
  #         temp = diminish(bar_list2, icon_list1)
  #         temp += connect(axes.coords_to_point(5.1, 1.6), axes.coords_to_point(5.1, 2.4))
  #         traffic(2.4, 5.1, 9.1, temp)
  #         temp = diminish(bar_list3, icon_list2)
  #         temp += survive(bar_list2, icon_list1)
  #         temp += connect(axes.coords_to_point(9.1, 2.4), axes.coords_to_point(9.1, 1.6))
  #         traffic(1.6, 9.1, 13.1, temp)
        
  #         temp = diminish(bar_list2, icon_list1)
  #         temp += survive(bar_list1, [])
  #         temp += connect(axes.coords_to_point(13.1, 1.6), axes.coords_to_point(13.1, 0.8))
  #         traffic(0.8, 13.1, 18, temp, "#12cc66", 0.07, False)

  #         self.wait(2)
  #         self.play(*[FadeOut(i) for i in dahsed_list + icon_list1 + icon_list2 + bar_list1 + bar_list2 + bar_list3])
          

  #         ########Traffic arrives
  #         bar_list1 = []
  #         bar_list2 = []
  #         bar_list3 = []
  #         icon_list1 = []
  #         icon_list2 = []
  #         dahsed_list = []


  #         def bare_traffic(thread, start, end, temp = [], color = "#029ffa", width = 0.07):
  #           box = Rectangle(height= 0.001, width=width, color=WHITE, stroke_width=0).move_to(axes.coords_to_point(start, thread), aligned_edge=UP)
  #           box.set_fill(color, opacity=1)
  #           height = axes.coords_to_point(start)[1] - axes.coords_to_point(end)[1]

  #           self.add(box)
  #           self.play(*temp, box.animate.set_height(height, about_edge=UP, stretch=True), run_time=0.5)
            
  #           if thread == 0.8:
  #             bar_list1.append(box)
  #           elif thread == 1.6:
  #             bar_list2.append(box)
  #           else:
  #             bar_list3.append(box)
  #           return box

  #         def traffic_jam(thread, start, end, dimish_list, color = "#df2c14", width = 0.07, icon = True):
  #           box = Rectangle(height= 0.001, width=width, color=WHITE, stroke_width=0).move_to(axes.coords_to_point(start, thread), aligned_edge=UP)
  #           box.set_fill(color, opacity=1)
  #           height = axes.coords_to_point(start)[1] - axes.coords_to_point(end)[1]

  #           self.add(box)
  #           self.play(*dimish_list, box.animate.set_height(height, about_edge=UP, stretch=True), run_time=0.5)
  #           bl = SVGMobject("cube.svg", stroke_width = 0).scale(0.12).move_to(axes.coords_to_point((start + end) / 2, thread)).shift(RIGHT*0.25)
  #           # self.play(ShowCreation(traffic1))
  #           bl2 = bl.copy().move_to(axes.coords_to_point((start + end) / 2, thread)).shift(RIGHT*0.25)

  #           if icon:
  #             self.play(FadeIn(bl), run_time=0.5)
  #             self.play(bl.animate.shift(UP*0.2), bl2.animate.shift(DOWN*0.2), run_time=0.5)
            
  #           if thread == 0.8:
  #             bar_list1.append(box)
  #           elif thread == 1.6:
  #             bar_list2.append(box)
  #             icon_list1.append(bl)
  #             icon_list1.append(bl2)
  #           else:
  #             bar_list3.append(box)
  #             icon_list2.append(bl)
  #             icon_list2.append(bl2)
  #           return box

  #         traffic(0.8, 0, 3.1, [], "#12cc66", 0.1, False)
  #         temp = diminish(bar_list1, [])

  #         temp += connect(axes.coords_to_point(3.1, 0.8), axes.coords_to_point(3.1, 1.6))
  #         traffic_jam(1.6, 3.1, 9.1, temp, "#df2c14")
  #         bare_traffic(1.6, 9.1, 9.3)
  #         temp = diminish(bar_list2, icon_list1)
  #         temp += connect(axes.coords_to_point(9.3, 1.6), axes.coords_to_point(9.3, 2.4))
  #         traffic_jam(2.4, 9.3, 15.3, temp, "#df2c14")
  #         bare_traffic(2.4, 15.3, 15.5)

        
  #         temp = diminish(bar_list3, icon_list2)
  #         temp += survive(bar_list2, icon_list1)
  #         temp += connect(axes.coords_to_point(15.5, 2.4), axes.coords_to_point(15.5, 1.6))

  #         bare_traffic(1.6, 15.5, 15.7, temp)

  #         temp = diminish(bar_list2, icon_list1)
  #         temp += survive(bar_list1, [])
  #         temp += connect(axes.coords_to_point(15.7, 1.6), axes.coords_to_point(15.7, 0.8))
  #         traffic(0.8, 15.7, 18, temp, "#12cc66", 0.07, False)

  #         self.play(FadeOut(m1), FadeOut(m2), FadeOut(client), FadeOut(label1), FadeOut(label2), FadeOut(label3), FadeOut(allts), FadeOut(axes), *[FadeOut(i) for i in dahsed_list + icon_list1 + icon_list2 + bar_list1 + bar_list2 + bar_list3])

  #         ###################### GNN
  #         self.remove(section)
          # section = Text("3 . Graph Neural Network", font=the_font, font_size=30).move_to([-6, 3.5, 0], aligned_edge=LEFT)
          # self.add(section)

          # nodes = []
          # edges = []
          # labels = []
          # def node(x, y, z):
          #   c = Circle()
          #   c.set_fill(BLUE, opacity=1)
          #   c.set_stroke(WHITE, width=1)
          #   c.set_width(0.1)
          #   c.move_to([x, y, 0])
          #   nodes.append(c)

          #   label = Text(str(z), font_size=30, font=the_font)
          #   if (z != "Frontend"):
          #     label.move_to(c).shift(DOWN * 0.2)
          #   else:
          #     label.move_to(c).shift(UP * 0.2)
          #   labels.append(label)

          
          # def edge(a, b):
          #   l = Line(a, b, stroke_width=1)
          #   edges.append(l)

          # node(0, 0, "Frontend")
          # node(-3, -1, "Cart")
          # node(-3, -2, "Recommendation")
          # node(-2, -3, "Product")
          # node(2, -3, "Shipping")
          # node(3, -1.5, "Currency")

          # edge(nodes[0], nodes[1])
          # edge(nodes[0], nodes[2])
          # edge(nodes[0], nodes[3])
          # edge(nodes[0], nodes[4])
          # edge(nodes[0], nodes[5])
          # edge(nodes[2], nodes[3])

          # graph = VGroup(VGroup(*edges, *nodes, *labels), Text("Online Boutique", font=the_font, t2s={"Online Boutique": ITALIC}))
          # graph.arrange(DOWN, buff=0.4)
          # graph.scale(0.7).move_to([-2, 0, 0])
          # self.add(graph)

          # node_matrix = Matrix([["1"], ["2"], ["1"], ["4"], ["3"]])
          # node_matrix.get_brackets().set_color(GREEN, PURPLE)
          # node_feature = VGroup(Text("Input Node Features:", font=the_font), node_matrix).arrange(RIGHT)
          # edge_matrix = Matrix([["145"], ["298"], ["153"], ["621"], ["465"], ["412"]])
          # edge_matrix.get_brackets().set_color(BLUE)
          # edge_feature = VGroup(Text("Input Edge Features:", font=the_font), edge_matrix).arrange(RIGHT)

          # features = VGroup(node_feature, edge_feature).arrange(DOWN)
          # features.next_to(graph).scale(0.5)
          # self.play(FadeIn(node_feature))

          # self.play(FadeIn(edge_feature))

          # all_cs = []
          # all_lines = []
          # def layer(x, color=BLUE):
          #   circles = VGroup()
          #   for i in range(x):
          #     c = Circle()
          #     c.set_fill(color, opacity=1)
          #     c.set_stroke(WHITE, width=1)
          #     c.set_width(0.2)
          #     circles.add(c)
          #   circles.arrange(DOWN, buff=0.15)
          #   all_cs.append(circles)
          #   return circles

          # def cross(a, b):
          #   temp = VGroup()
          #   for i in a:
          #     for j in b:
          #       l = Line(i, j, stroke_color=WHITE, opacity=0.5, stroke_width = 0.1)
          #       temp.add(l)
          #       all_lines.append(l)
          #   return temp

          # a = layer(5, GREEN)
          # b = layer(5, GREEN)
          # b.next_to(a, buff=1.6)
          # f = layer(5, GREEN)
          # f.next_to(b, buff=1.6)

          # c = layer(6)
          # d = layer(6)
          # e = layer(6)
          # d.next_to(c, buff=1)
          # e.next_to(d, buff=1)
          # g = layer(5, PURPLE)
          # g.next_to(e, buff = 1)

          # add_lines = VGroup()
          # f1 = layer(5, ORANGE)
          # f2 = layer(1, ORANGE)
          # final = VGroup(f1, f2)
          # final.arrange(RIGHT).shift(RIGHT * 2.5)

          # node_label = Text("Node pooling", font=the_font, font_size=20)
          # greens = VGroup(node_label, VGroup(a, b, f, cross(a, b), cross(b, f)))
          # greens.arrange(DOWN)
          # node_label.shift(RIGHT * 1.6)

          # edge_label = Text("Edge pooling", font=the_font, font_size=20)
          # blues = VGroup(edge_label, VGroup(c, d, e, g, cross(c, d), cross(d, e), cross(e, g)))
          # blues.arrange(DOWN)
          # edge_label.shift(RIGHT*1)
        
          # gnn1 = VGroup(greens, blues)
          # gnn1.arrange(DOWN, buff=0.5, aligned_edge=LEFT)

          # count = 0
          # for i in (g):
          #   temp = Line(i, f1[count], stroke_color=WHITE, opacity=0.5, stroke_width = 0.1)
          #   add_lines.add(temp)
          #   all_lines.append(temp)
          #   count += 1
          
          # count = 0
          # for i in (f):
          #   temp = Line(i, f1[count], stroke_color=WHITE, opacity=0.5, stroke_width = 0.1)
          #   add_lines.add(temp)
          #   all_lines.append(temp)
          #   count += 1

          # big_gnn = VGroup(*all_cs, *all_lines)
          # big_gnn.shift(RIGHT * 1.5)


          # #######################
          # #######################
          # graph.generate_target()
          # graph.target.scale(0.6)
          # graph.target.shift(LEFT * 2)

          # for i, j in [(node_matrix, a), (edge_matrix, c)]:
          #   i.generate_target()
          #   i.target.scale(0.83)
          #   i.target.next_to(j, aligned_edge=RIGHT).shift(LEFT * 1)

          # self.remove(features)
          # self.play(MoveToTarget(graph), MoveToTarget(node_matrix), MoveToTarget(edge_matrix))

          # projection = Text("Projection", font=the_font, font_size=20)
          # addtext = Text("Add", font=the_font, font_size=20)
          # addtext.move_to(add_lines).rotate(-62 * DEGREES)
          # addtext.shift(UP * 1.5 + RIGHT * 0.2)
          # projection.move_to(g).rotate(-8 * DEGREES)
          # projection.shift(LEFT * 0.6 + UP * 1)
          # latency = Text("Latency", font=the_font, font_size=20)
          # latency.move_to(f2).shift(0.5* RIGHT)
          # self.play(ShowCreation(greens), ShowCreation(blues), FadeIn(projection))

          # self.play(ShowCreation(final), ShowCreation(cross(f1, f2)), ShowCreation(add_lines), FadeIn(addtext), FadeIn(latency))

          # final = VGroup(f1, f2, cross(f1, f2))
          
          ###################### GNN
          self.remove(section)
          section = Text("5. Results", font=the_font, font_size=30).move_to([-6, 3.5, 0], aligned_edge=LEFT)
          self.add(section)


          # magic_number = 0.8
          
          axes = NumberPlane(
              x_range=[0, 18, 1],
              y_range=[0, 6, 1],
              height = 3,
              width = 4.9,
              tips=False,
              faded_line_ratio = 4,
              # color= "#f5f5f5",
              color="#000000",
              axis_config={"include_numbers": False},
              # x_axis_config = {"include_ticks": True},
              background_line_style={
                  "stroke_color": BLACK,
                  "stroke_width": 2,
                  "stroke_opacity": 0.6
              },
              faded_line_style={
                "stroke_color": BLACK,
              }
              # y_axis_config={"scaling": LogBase(custom_labels=True)},
            ).rotate(-90 * DEGREES, about_edge=IN).shift(LEFT*4)

          client = axes.get_graph(
            lambda x: 0.8,
            color="#B2BEB5",
            stroke_width=0.2,
            opacity=0.5,
          )
          # client = DashedVMobject(client)
          m1 = axes.get_graph(
            lambda x: 1.6,
            color="#B2BEB5",
            stroke_width = 0.2,
          )
          m2 = axes.get_graph(
            lambda x: 2.4,
            color="#B2BEB5",
            stroke_width = 0.2,
          )


          def traffic(thread, start, end, dimish_list, color = "#029ffa", width = 0.07, icon = True):
            box = Rectangle(height= 0.001, width=width, color=WHITE, stroke_width=0).move_to(axes.coords_to_point(start, thread), aligned_edge=UP)
            box.set_fill(color, opacity=1)
            height = axes.coords_to_point(start)[1] - axes.coords_to_point(end)[1]

            self.add(box)
            self.play(*dimish_list, box.animate.set_height(height, about_edge=UP, stretch=True), run_time=0.5)
            bl = SVGMobject("document.svg").scale(0.2).move_to(axes.coords_to_point((start + end) / 2, thread)).shift(RIGHT*0.25)
            # self.play(ShowCreation(traffic1))
            if icon:
              self.play(FadeIn(bl))
            
            if thread == 0.8:
              bar_list1.append(box)
            elif thread == 1.6:
              bar_list2.append(box)
              icon_list1.append(bl)
            else:
              bar_list3.append(box)
              icon_list2.append(bl)
            return box

          # self.play(ShowCreation(step_graph))
          # axes.add_coordinate_labels(
          #     font_size=20,
          #     font = the_font,
          #     num_decimal_places=1,
          # )


          def add_text(content, thread, a = 0):
            client_t = Text(content, font=the_font, font_size=10).move_to(axes.coords_to_point(0, thread), aligned_edge=DOWN).shift(UP*0.13).rotate(20*DEGREES)
            self.add(client_t)
            return client_t

          label1 = add_text("Frontend", 0.8)
          label2 = add_text("Cart", 1.6, 0.5)
          label3 = add_text("Recommendation", 2.4)
          label4 = add_text("Product", 3.2, 0.5)
          label5 = add_text("Shipping", 4)
          label6 = add_text("Currency", 4.8, 0.5)


          self.play(FadeIn(axes))
          self.play(ShowCreation(m1), ShowCreation(m2), ShowCreation(client))
          def diminish(bar_list, icon_list):
            animation_list = []
            for box in bar_list:
              box.generate_target()
              box.target.set_width(0.02, about_edge=UP, stretch=True)
              box.target.set_opacity(0.5)
              animation_list.append(MoveToTarget(box))
            for bl in icon_list:
              bl.generate_target()
              bl.target.set_opacity(0.5)
              bl.target.scale(0.8)
              animation_list.append(MoveToTarget(bl))
            return animation_list

          def survive(bar_list, icon_list):
            animation_list = []
            for box in bar_list:
              box.generate_target()
              box.target.set_width(0.07, about_edge=UP, stretch=True)
              box.target.set_opacity(1)
              animation_list.append(MoveToTarget(box))
            for bl in icon_list:
              bl.generate_target()
              bl.target.set_opacity(1)
              bl.target.scale(1.25)
              animation_list.append(MoveToTarget(bl))
            return animation_list

          def connect(start, end):
            dashed = DashedLine(start, end, color="#FFFFFF", stroke_width=0.5)
            dahsed_list.append(dashed)
            return [ShowCreation(dashed)]

          ########Traffic arrives
          bar_list1 = []
          bar_list2 = []
          bar_list3 = []
          icon_list1 = []
          icon_list2 = []
          dahsed_list = []
          traffic(0.8, 0, 3.1, [], "#12cc66", 0.1, False)
          temp = diminish(bar_list1, [])



          temp += connect(axes.coords_to_point(3.1, 0.8), axes.coords_to_point(3.1, 1.6))
          traffic(1.6, 3.1, 5.1, temp)
          temp = diminish(bar_list2, icon_list1)
          temp += connect(axes.coords_to_point(5.1, 1.6), axes.coords_to_point(5.1, 2.4))
          traffic(2.4, 5.1, 9.1, temp)
          temp = diminish(bar_list3, icon_list2)
          temp += survive(bar_list2, icon_list1)
          temp += connect(axes.coords_to_point(9.1, 2.4), axes.coords_to_point(9.1, 1.6))
          traffic(1.6, 9.1, 13.1, temp)
        
          temp = diminish(bar_list2, icon_list1)
          temp += survive(bar_list1, [])
          temp += connect(axes.coords_to_point(13.1, 1.6), axes.coords_to_point(13.1, 0.8))
          traffic(0.8, 13.1, 18, temp, "#12cc66", 0.07, False)

          self.wait(2)
          self.play(*[FadeOut(i) for i in dahsed_list + icon_list1 + icon_list2 + bar_list1 + bar_list2 + bar_list3])



          while True:
            self.wait(10)
          
TextExample().construct()

