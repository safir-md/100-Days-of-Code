def turn_right():
    turn_left()
    turn_left()
    turn_left()

while(not is_facing_north()):
    turn_left()
while(not at_goal()):
    if(at_goal()):
        done()
    elif(right_is_clear()):
        turn_right()
        while(right_is_clear()):
            move()
    elif(wall_in_front() and wall_on_right()):
        while(not front_is_clear()):
            turn_left()
    else:
        move()
