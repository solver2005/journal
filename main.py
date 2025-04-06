from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint


class Ball(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

class Paddle(Widget):
    score = NumericProperty(0)
    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            ball.velocity_x *= -1.1
        if ball.velocity_x > 15:
            ball.velocity_x = 15

class Sch(Widget):
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)
    def serve_ball(self):
        rot = randint(0, 360)
        while(rot>60 and rot < 120) or (rot<210 and rot>150):
            rot = randint(0, 360)
        self.ball.velocity = Vector(4, 0).rotate(rot)
    def update(self, fps):
        self.ball.move()
        if self.ball.y < 0 or self.ball.y > self.height-50:
            self.ball.velocity_y *= -1
        if self.ball.x < 0:
            self.ball.velocity_x *= -1
            self.player2.score+=1
        if self.ball.x > self.width-50:
            self.ball.velocity_x *= -1
            self.player1.score+=1

        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)

    def on_touch_move(self, touch):
        if touch.x < self.width / 4:
            self.player1.center_y = touch.y
        if touch.x > self.width *3/4:
            self.player2.center_y = touch.y
class SchApp(App):
    def build(self):
        game = Sch()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game

SchApp().run()