def solution():
    xena_start = 600
    dragon_start = 0
    burn_range = 120
    xena_speed = 15
    dragon_speed = 30

    # Calculate the distance Xena needs to run to reach the cave
    distance_to_cave = xena_start - burn_range

    # Calculate how long it will take Xena to reach the cave at her speed
    xena_time = distance_to_cave / xena_speed

    # Calculate how far the dragon can fly during that time
    dragon_distance = xena_time * dragon_speed

    # If the dragon can still burn Xena, she doesn't make it to the cave in time
    if dragon_distance >= (xena_start - burn_range):
        return "Xena doesn't make it to the cave in time."

    result = xena_time
    return result

print(solution())