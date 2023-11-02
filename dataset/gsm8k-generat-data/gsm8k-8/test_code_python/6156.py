def solution():
    total_distance = 60 * 3  # distance = speed * time
    remaining_distance = total_distance - (60 * 2)  # distance remaining after the first 3 hours
    required_average_speed = 70  # given in problem

    # We can use the formula: total_distance = (speed_avg * total_time)
    # to find the speed required for the remaining 2 hours
    required_speed = (required_average_speed * 5) - 60  # speed = distance / time

    result = required_speed
    return result

print(solution())