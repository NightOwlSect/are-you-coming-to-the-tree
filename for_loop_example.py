import turtle

# Set up the screen window
window = turtle.Screen()

# Create a visible turtle object
my_turtle = turtle.Turtle()
my_turtle.shapesize(3)

def click_handler(x, y):
  my_turtle.clear()
  my_turtle.speed(0)
  # fastest speed

  my_turtle.pendown()
  for i in range(4):
    my_turtle.forward(100)
    my_turtle.right(90)
  my_turtle.penup()

my_turtle.onclick(click_handler)

# Keep the window open and listening for events
window.mainloop()
