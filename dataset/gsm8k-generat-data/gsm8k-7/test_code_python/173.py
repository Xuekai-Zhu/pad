def solution():
    hare_speed = 10  # feet per second
    turtle_speed = 1  # feet per second
    race_distance = 20  # feet

    # Calculate the time it takes for the hare to run the race
    hare_time = race_distance / hare_speed

    # Calculate the distance the turtle can crawl in the time it takes for the hare to run the race
    turtle_distance = turtle_speed * hare_time

    # Calculate the head start the turtle needs to finish in a tie with the hare
    turtle_head_start = race_distance - turtle_distance
    turtle_head_start /= turtle_speed

    result = turtle_head_start
    return result

print(solution())