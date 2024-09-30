#   a116_buggy_image.py
import turtle as trtl

#Creating spider body
painter = trtl.Turtle()
painter.pensize(40)
painter.circle(20)

#Creating the variables for legs
leg_amount = 8
leg_length = 70
angle_between_legs = 360 / leg_amount
painter.pensize(5)
leg_counter = 0

#Creating/counting spider legs
while (leg_counter < leg_amount):
  painter.goto(0,20)
  painter.setheading(angle_between_legs * leg_counter)
  painter.forward(leg_length)
  leg_counter = leg_counter + 1
painter.hideturtle()
wn = trtl.Screen()
wn.mainloop()