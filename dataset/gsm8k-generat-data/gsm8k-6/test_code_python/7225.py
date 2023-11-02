def solution():
    # Calculate the distance traveled in normal space and through the black hole separately
    normal_space_distance = 2 * 7  # 2 billion miles per hour for 7 hours
    black_hole_distance = 3 * normal_space_distance  # traveling three times faster in a black hole

    # Calculate the total distance traveled
    total_distance = normal_space_distance + black_hole_distance

    # Convert the total distance from miles to billion miles
    total_distance_billion_miles = total_distance / (10 ** 9)

    result = total_distance_billion_miles
    return result

print(solution())