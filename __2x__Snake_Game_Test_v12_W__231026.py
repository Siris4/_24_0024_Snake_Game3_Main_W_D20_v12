
from turtle import Screen
from Snake_Class_Module_v01_W_231025 import Snake
from Food_Module_v01_W import Food
from ScoreBoard_v01_W import Scoreboard
import time

# game_on = False

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Siris's Snake Game")    #lables the Title of the pop-up window!


# TODO 1: Create the Snake (object) Body from a Snake Class

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()  # it must listen first before triggering functions with key-typing
# to trigger the function in the moment a key is pressed, remove the additional ()  !!


screen.onkey(fun=snake.go_west, key="Left")
screen.onkey(fun=snake.go_east, key="Right")
screen.onkey(fun=snake.go_up, key="Up")
screen.onkey(fun=snake.go_down, key="Down")
# screen.onkey(fun=Turtle.reset_board, key="r")

game_on = True
while game_on:
    screen.update()  #if we move this update Method OUTSIDE of the for loop (just below), it basically waits for ALL segments to move forwards first, and THEN generates a screen refresh.
    time.sleep(0.1)  #also, instead of having it delay by 1 second for each SEGMENT individually (as originally placed in the for loop below), change it to 1 sec, after ALL segments have officially shifted, to make this go by a little faster.
                          # right now, our segments are not linked, they are indivially doing their own object instance motions! The first block would turn, but the other 2 would continue to move forward in a straight line.
                                # so ideally, we want them to all be linked together, so we could have segment[2] take over for segment[1]'s spot, and seg[1] take over for the seg[0] spot. Then we control the first segment, where it moves forwards, and the rest follows!
                #so we basically begin a loop, starting from the end, and going to the #1 segment (head of the snake) - reverse order
    snake.move()


    #Detect collision with food: turtle.distance()
    if snake.head.distance(food) < 15:
        food.respawn_food_location()
        scoreboard.update_score()    # not Scoreboard Class. you want to access the scoreboard (object) to modify it's value. You're not trying to modify the Class itself.




screen.exitonclick()
