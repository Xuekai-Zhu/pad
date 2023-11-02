def solution():
    rabbit_speed = 25  # Rabbit's speed in miles per hour
    cat_speed = 20  # Cat's speed in miles per hour
    head_start_distance = (cat_speed / 4)  # Distance the cat runs during its 15-minute head start
    distance_to_catch_up = head_start_distance  # Distance the rabbit needs to catch up to the cat
    time_to_catch_up = distance_to_catch_up / (rabbit_speed - cat_speed)  # Time it takes for the rabbit to catch up, in hours
    result = time_to_catch_up
    return result

print(solution())