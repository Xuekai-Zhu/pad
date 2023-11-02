def solution():
    """Mark has two pets, a hare that runs 10 feet/second and a turtle that crawls 1 foot/second. If they're going to run a 20 foot-race, how much of a head start (in seconds) does the turtle need to finish in a tie?"""
    # Define the speed of the hare and turtle
    hare_speed = 10
    turtle_speed = 1

    # Define the distance of the race
    race_distance = 20

    # Calculate the time it takes for the hare and turtle to finish the race
    hare_time = race_distance / hare_speed
    turtle_time = race_distance / turtle_speed

    # Calculate the head start the turtle needs to finish in a tie
    head_start = hare_time - turtle_time

    # Return the result
    result = head_start
    return result

print(solution())