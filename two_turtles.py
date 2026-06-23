import turtle

# Create the screen
window = turtle.Screen()
window.setup(600, 400)
window.title("Turtles drawing moving patterns")
window.tracer(0)

# Create turtles
left_turtle = turtle.Turtle()
left_turtle.shape("turtle")
left_turtle.color("red")
left_turtle.penup()
left_turtle.goto(-140, 0)
left_turtle.pendown()

right_turtle = turtle.Turtle()
right_turtle.shape("turtle")
right_turtle.color("blue")
right_turtle.penup()
right_turtle.goto(140, 0)
right_turtle.pendown()

center_turtle = turtle.Turtle()
center_turtle.shape("turtle")
center_turtle.color("green")
center_turtle.penup()
center_turtle.goto(0, 120)
center_turtle.pendown()

bottom_turtle = turtle.Turtle()
bottom_turtle.shape("turtle")
bottom_turtle.color("orange")
bottom_turtle.penup()
bottom_turtle.goto(0, -120)
bottom_turtle.pendown()

square_turtle = turtle.Turtle()
square_turtle.shape("turtle")
square_turtle.color("purple")
square_turtle.penup()
square_turtle.goto(-200, -150)
square_turtle.pendown()


def draw_pattern(t, size, angle):
    for _ in range(6):
        t.forward(size)
        t.right(angle)
        t.forward(4)
        t.right(20)

    # After finishing one full loop, turn and keep moving
    t.right(100)
    t.forward(8)


spiral_index = 0


def spiral_move(t):
    global spiral_index
    t.pendown()
    if spiral_index < 1000:
        t.forward(spiral_index / 15)
        t.right(10)
        spiral_index += 1


def draw_square_spiral(t):
    for i in range(1, 40):
        t.forward(i * 3)
        t.right(90)


def animate():
    draw_pattern(left_turtle, 50, 36)
    draw_pattern(right_turtle, 50, 45)
    draw_pattern(center_turtle, 50, 67)
    spiral_move(bottom_turtle)
    draw_square_spiral(square_turtle)

    window.update()
    window.ontimer(animate, 20)


animate()
window.mainloop()
