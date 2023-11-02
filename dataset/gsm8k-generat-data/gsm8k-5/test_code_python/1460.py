def solution():
    total_distance = 24  # The journey is 24 km
    total_time = 8  # The man intends to complete the journey in 8 hours
    distance_covered_in_first_four_hours = 4 * 4  # The man covers 4 km/hr in the first 4 hours
    remaining_distance = total_distance - distance_covered_in_first_four_hours  # The remaining distance to cover
    remaining_time = total_time - 4  # The remaining time to cover the remaining distance

    # Calculate the speed the man needs to travel to cover the remaining distance in the remaining time
    required_speed = remaining_distance / remaining_time
    result = required_speed
    return result

print(solution())