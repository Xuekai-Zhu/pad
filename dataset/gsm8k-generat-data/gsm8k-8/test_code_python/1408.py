def solution():
    # Calculate the total distance for the first half of the year
    first_half_distance = 20 * 26  # 26 weeks in half a year

    # Calculate the total distance for the second half of the year
    second_half_distance = 30 * 26  # 26 weeks in half a year

    # Calculate the total distance for the whole year
    total_distance = first_half_distance + second_half_distance
    result = total_distance
    return result

print(solution())