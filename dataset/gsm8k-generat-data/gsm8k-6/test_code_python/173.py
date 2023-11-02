def solution():
    # Calculate the time it takes for the hare to run 20 feet
    hare_time = 20 / 10  # hare's speed is 10 feet/second

    # Calculate the distance the turtle can cover in that time
    turtle_distance = 1 * hare_time  # turtle's speed is 1 foot/second

    # Calculate the time the turtle needs to finish the race
    turtle_time = 20 / turtle_distance

    # Calculate the head start the turtle needs to finish in a tie
    head_start = turtle_time - hare_time
    result = head_start
    return result

print(solution())