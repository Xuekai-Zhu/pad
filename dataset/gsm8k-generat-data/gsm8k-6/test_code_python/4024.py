def solution():
    # Calculate Jodi's total distance walked in 4 weeks
    week_1_distance = 1 * 6  # Jodi walks 1 mile a day for 6 days in the first week
    week_2_distance = 2 * 6  # Jodi walks 2 miles a day for 6 days in the second week
    week_3_distance = 3 * 6  # Jodi walks 3 miles a day for 6 days in the third week
    week_4_distance = 4 * 6  # Jodi walks 4 miles a day for 6 days in the fourth week
    total_distance = week_1_distance + week_2_distance + week_3_distance + week_4_distance
    result = total_distance
    return result

print(solution())