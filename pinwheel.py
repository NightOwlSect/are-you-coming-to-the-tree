import turtle

# Set up the screen window
window = turtle.Screen()

# Create a visible turtle object
my_turtle = turtle.Turtle()
my_turtle.shapesize(3)

def pinwheel(sides, size=100, backup=0):
  for _ in range(sides):
    my_turtle.forward(size)
    my_turtle.forward(-backup)
    my_turtle.right(360/sides)

def click_handler(x, y):
  my_turtle.clear()
  my_turtle.speed(0)
  # fastest speed

  my_turtle.pendown()
  pinwheel(7)
  my_turtle.penup()

my_turtle.onclick(click_handler)

# Keep the window open and listening for events
window.mainloop()
