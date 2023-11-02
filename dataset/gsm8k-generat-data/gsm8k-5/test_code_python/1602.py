def solution():
    total_distance = 8205  # The distance across the country is 8205 km
    distance_covered = 907 + 582  # Amelia drove 907 km on Monday and 582 km on Tuesday
    distance_remaining = total_distance - distance_covered  # Calculate the distance still remaining

    result = distance_remaining
    return result

print(solution())