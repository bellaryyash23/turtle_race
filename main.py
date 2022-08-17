from turtle import Turtle, Screen
import random

race_on = False
screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your Bet!!", prompt="Which turtle will win the race? Enter a  color: ")
colors = ["red", "orange", "yellow", "green", "purple", "blue"]
turtle_names = ["red", "orange", "yellow", "green", "purple", "blue"]

for i in range(0, 6):
    turtle_names[i] = Turtle(shape="turtle")
    turtle_names[i].penup()
    turtle_names[i].color(colors[i])
    turtle_names[i].goto(x=-230, y=-120+50*i)

if user_bet:
    race_on = True

while race_on:
    for turtle_name in turtle_names:
        if turtle_name.xcor() > 230:
            race_on = False
            winning_turtle = turtle_name.pencolor()
            if winning_turtle == user_bet:
                print(f"You Won!!! The {winning_turtle} turtle is the winner!")
                break
            else:
                print(f"You Lost!!! The {winning_turtle} turtle is the winner!")
                break
        rand_dist = random.randint(0, 10)
        turtle_name.forward(rand_dist)

screen.exitonclick()
