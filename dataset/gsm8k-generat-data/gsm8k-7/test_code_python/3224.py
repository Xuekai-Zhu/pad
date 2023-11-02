def solution():
    speed_1 = 16  # miles per hour
    speed_2 = 12  # miles per hour
    speed_3 = 20  # miles per hour
    time = 15  # minutes
    distance_1 = (speed_1 * time) / 60  # miles
    distance_2 = (speed_2 * time) / 60  # miles
    distance_3 = (speed_3 * time) / 60  # miles
    total_distance = distance_1 + distance_2 + distance_3
    result = total_distance
    return result

print(solution())