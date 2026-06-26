import turtle
import colorsys


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

all_turtles = [left_turtle, right_turtle, center_turtle, bottom_turtle, square_turtle]
start_positions = {}
hue = 0.0


def update_background_color():
    global hue
    hue = (hue + 0.005) % 1.0
    r, g, b = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
    window.bgcolor((r, g, b))

for t in all_turtles:
    start_positions[t] = (t.xcor(), t.ycor(), t.heading())


def reset_turtle(t):
    x, y, heading = start_positions[t]
    t.clear()
    t.penup()
    t.goto(x, y)
    t.setheading(heading)
    t.pendown()
    window.update()


def reset_after_delay(t):
    window.ontimer(lambda: reset_turtle(t), 5000)


slinky_state = {}


def draw_slinky_motion(t, base_radius, turn_amount):
    t.pendown()
    t.pensize(2)

    state = slinky_state.setdefault(
        t,
        {"radius": base_radius, "turn": turn_amount},
    )

    t.circle(state["radius"], 25)
    state["radius"] = max(2, state["radius"] - 0.15)
    if state["radius"] <= 2:
        state["radius"] = base_radius
    t.right(turn_amount)


def draw_cube():
    reset_after_delay(left_turtle)
    left_turtle.clear()
    left_turtle.penup()
    left_turtle.speed(0)
    left_turtle.pensize(3)
    left_turtle.color("gray")

    left_turtle.goto(-80, -60)
    left_turtle.pendown()
    for _ in range(4):
        left_turtle.forward(70)
        left_turtle.left(90)

    left_turtle.penup()
    left_turtle.goto(-50, -30)
    left_turtle.pendown()
    for _ in range(4):
        left_turtle.forward(70)
        left_turtle.left(90)

    left_turtle.penup()
    left_turtle.goto(-80, -60)
    left_turtle.pendown()
    left_turtle.goto(-50, -30)
    left_turtle.goto(20, -30)
    left_turtle.goto(-10, -60)
    left_turtle.goto(-80, -60)

    window.update()


def draw_bubble(t):
    reset_after_delay(t)
    t.clear()
    t.penup()
    t.speed(0)
    t.pensize(3)

    t.color("lightblue")
    t.goto(0, 0)
    t.pendown()
    t.circle(30)

    t.penup()
    t.goto(10, 12)
    t.pendown()
    t.color("white")
    t.circle(8)

    window.update()


for t in all_turtles:
    t.onclick(lambda x, y, current_turtle=t: draw_bubble(current_turtle), add=False)


def animate():
    update_background_color()
    draw_slinky_motion(left_turtle, 24, 12)
    draw_slinky_motion(right_turtle, 20, 10)
    draw_slinky_motion(center_turtle, 18, 8)
    draw_slinky_motion(bottom_turtle, 16, 6)
    draw_slinky_motion(square_turtle, 14, 5)

    window.update()
    window.ontimer(animate, 40)


window.onkeypress(draw_cube, "space")
window.listen()
animate()
window.mainloop()
