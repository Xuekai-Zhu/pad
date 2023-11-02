def solution():
    distance_day1 = 5 * 7  # Barry and Jim travel at 5 mph for 7 hours on the first day
    distance_day2_part1 = 6 * 6  # They travel at 6 mph for 6 hours on the second day
    distance_day2_part2 = 3 * 3  # Then they travel at 3 mph for 3 hours on the second day
    distance_day3 = 7 * 5  # They travel at 7 mph for 5 hours on the third day

    # Calculate the total distance traveled
    total_distance = distance_day1 + distance_day2_part1 + distance_day2_part2 + distance_day3
    result = total_distance
    return result

print(solution())