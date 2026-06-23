import turtle
from functools import partial

# Set up the screen window
window = turtle.Screen()

# Create a visible turtle object
turtle1 = turtle.Turtle()
turtle1.shapesize(3)

def pinwheel(a_turtle, sides, size=100, backup=0):
  for _ in range(sides):
    a_turtle.forward(size)
    a_turtle.forward(-backup)
    a_turtle.right(360/sides)

def click_handler(x, y):
  window.tracer(0)
  turtle1.clear()
  turtle1.speed(0)
  # fastest speed

  turtle1.pendown()
  for i in range(500):
    turtle1.clear()
    pinwheel(turtle1, 7, 100, i/5)
    window.update()
  turtle1.penup()

turtle1.onclick(click_handler)

# Keep the window open and listening for events
window.mainloop()
