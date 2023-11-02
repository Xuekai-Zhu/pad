def solution():
    # Calculate Xena's running speed and the dragon's flying speed
    xena_speed = 15
    dragon_speed = 30

    # Calculate the distance the dragon needs to fly to get within 120 feet of Xena
    danger_distance = 600 - 120

    # Calculate how long it takes the dragon to cover that distance
    danger_time = danger_distance / dragon_speed

    # Calculate how far Xena can run in that amount of time
    xena_distance = xena_speed * danger_time

    # Calculate how long it takes Xena to reach the cave, accounting for her head start
    time_to_cave = (600 + xena_distance) / xena_speed

    result = time_to_cave
    return result

print(solution())