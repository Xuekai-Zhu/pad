def solution():
    """Mark has two pets, a hare that runs 10 feet/second and a turtle that crawls 1 foot/second. If they're going to run a 20 foot-race, how much of a head start (in seconds) does the turtle need to finish in a tie?"""
    hare_speed = 10
    turtle_speed = 1
    race_distance = 20
    time_taken_by_hare = race_distance / hare_speed
    time_taken_by_turtle = race_distance / turtle_speed
    head_start_for_turtle = (time_taken_by_hare - time_taken_by_turtle)
    result = head_start_for_turtle
    return result

print(solution())