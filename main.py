from turtle import Screen
from snake import Snake
from food import Food
import time
from scoreboard import ScoreBoard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
# THE SCREEN IS NOT GOING TO REFRESH UNTIL WE CALL A COMMAND "UPDATE".
screen.tracer(0)
# TRACER ALLOWS USER TO SHOW OBJECTS ON SCREEN USING COMMANDS

starting_positions = [(0, 0), (-20, 0), (-40, 0)]


snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)  # DELAYS THE TURTLE FOR 1 SECOND
    snake.move()   

    # DETECT COLLISION WITH FOOD
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # DETECT COLLISION WITH WALL.
    if snake.head.xcor() > 300 or snake.head.xcor() <-300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        scoreboard.reset()
        snake.reset()

    # DETECT COLLISION WITH TAIL.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10 :
            scoreboard.reset()
            snake.reset()
            
           

screen.exitonclick()
