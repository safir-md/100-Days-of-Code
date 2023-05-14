def jump():
    turn_left()
    while(not right_is_clear()):
        move()
    turn_right()
    move()
    turn_right()
    while(not wall_in_front()):
        move()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while(not at_goal()):
    if(at_goal()):
        done()
    if(wall_in_front()):
        jump()
    if(front_is_clear()):
        move()
