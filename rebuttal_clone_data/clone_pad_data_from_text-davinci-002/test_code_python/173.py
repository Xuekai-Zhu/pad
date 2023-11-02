def solution():
    """Mark has two pets, a hare that runs 10 feet/second and a turtle that crawls 1 foot/second. If they're going to run a 20 foot-race, how much of a head start (in seconds) does the turtle need to finish in a tie?"""
    rabbit_speed = 10
    turtle_speed = 1
    race_length = 20
    
    time_rabbit = race_length / rabbit_speed
    time_turtle = race_length / turtle_speed
    
    difference = time_rabbit - time_turtle
    head_start = difference / 2
    
    result = head_start
    
    return result

print(solution())