def solution():
    total_distance = 70
    day1_distance = total_distance * 0.2
    remaining_distance = total_distance - day1_distance
    day2_distance = remaining_distance * 0.5
    day3_distance = total_distance - day1_distance - day2_distance
    result = day3_distance
    return result

print(solution())