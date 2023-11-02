def solution():
    """Xena is trying to outrun a dragon to get to the safety of a cave it's too big to fit into. Xena has a 600 foot head start, but the dragon can burn her if it gets within 120 feet of her. If Xena runs 15 feet per second and the dragon flies 30 feet per second, how many seconds does Xena have to get to the cave?"""
    # Define Xena's initial distance from the cave and the dragon's burn range
    xena_distance = 600
    burn_range = 120

    # Define Xena's speed and the dragon's speed
    xena_speed = 15
    dragon_speed = 30

    # Calculate how long it takes the dragon to reach Xena's starting point
    dragon_time_to_start = xena_distance / dragon_speed

    # Calculate Xena's distance from the dragon when the dragon reaches her starting point
    xena_distance_from_dragon = dragon_time_to_start * xena_speed

    # Calculate how long Xena has to get to the cave
    time_to_cave = (xena_distance - burn_range - xena_distance_from_dragon) / xena_speed

    # Display how long Xena has to get to the cave
    result = time_to_cave
    return result

print(solution())