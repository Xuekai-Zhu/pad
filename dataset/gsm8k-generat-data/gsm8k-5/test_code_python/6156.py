def solution():
    total_distance = 60 * 3  # The man drives 60 mph for 3 hours
    remaining_distance = (70 * 5) - total_distance  # The man needs to cover this distance in the next 2 hours to get an average speed of 70 mph
    required_speed = remaining_distance / 2  # Calculate the speed required to cover the remaining distance in 2 hours
    result = required_speed
    return result

print(solution())