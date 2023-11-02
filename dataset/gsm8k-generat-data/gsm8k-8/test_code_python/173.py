def solution():
    hare_speed = 10  # feet per second
    turtle_speed = 1  # feet per second
    race_distance = 20  # feet

    # Time it takes for the hare to run the race
    hare_time = race_distance / hare_speed

    # Distance the turtle can crawl during that time
    turtle_distance = turtle_speed * hare_time

    # Head start the turtle needs to finish in a tie
    head_start = (race_distance - turtle_distance) / turtle_speed

    result = head_start
    return result

print(solution())