def solution():
    hare_speed = 10  # Hare runs 10 feet/second
    turtle_speed = 1  # Turtle crawls 1 foot/second
    race_distance = 20  # The race distance is 20 feet

    # Calculate the time it takes for the hare to finish the race
    hare_time = race_distance / hare_speed

    # Calculate the head start the turtle needs to finish in a tie
    turtle_head_start = hare_time * turtle_speed
    result = turtle_head_start
    return result

print(solution())