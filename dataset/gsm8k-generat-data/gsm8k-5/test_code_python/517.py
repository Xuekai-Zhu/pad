def solution():
    morning_distance = 2  # Roger rode his bike for 2 miles in the morning
    evening_distance = 5 * morning_distance  # Roger rode 5 times the morning distance in the evening

    # Calculate the total distance Roger rode that day
    total_distance = morning_distance + evening_distance
    result = total_distance
    return result

print(solution())