def solution():
    """Mark has two pets, a hare that runs 10 feet/second and a turtle that crawls 1 foot/second. If they're going to run a 20 foot-race, how much of a head start (in seconds) does the turtle need to finish in a tie?"""
    # Define the speeds of the hare and turtle
    hare_speed = 10  # feet per second
    turtle_speed = 1  # feet per second

    # Define the distance of the race
    race_distance = 20  # feet

    # Calculate the time it takes for the hare to finish the race
    hare_time = race_distance / hare_speed

    # Calculate the time it takes for the turtle to finish the race with a head start
    turtle_headstart = 0
    turtle_time = 0
    while hare_time > turtle_time:
        turtle_headstart += 1
        turtle_time = (race_distance - turtle_headstart) / turtle_speed

    # Return the head start needed for the turtle to finish in a tie
    result = turtle_headstart
    return result

print(solution())