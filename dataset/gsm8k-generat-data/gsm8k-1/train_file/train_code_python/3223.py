def solution():
    """Stephen rides his bicycle to church. During the first third of his trip, he travels at a speed of 16 miles per hour. During the second third of his trip, riding uphill, he travels a speed of 12 miles per hour. During the last third of his trip, he rides downhill at a speed of 20 miles per hour. If each third of his trip takes 15 minutes, what is the distance Stephen rides his bicycle to church, in miles?"""
    time_per_third = 15 / 60  # convert 15 minutes to hours
    speed_first_third = 16
    speed_second_third = 12
    speed_third_third = 20
    distance_first_third = speed_first_third * time_per_third
    distance_second_third = speed_second_third * time_per_third
    distance_third_third = speed_third_third * time_per_third
    total_distance = distance_first_third + distance_second_third + distance_third_third
    result = total_distance
    return result

print(solution())