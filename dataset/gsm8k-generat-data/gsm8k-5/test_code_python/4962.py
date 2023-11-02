def solution():
    days_in_two_weeks = 14  # Kendra wants to do laundry once every two weeks
    total_shirts_per_day = 5  # Kendra wears one shirt to school each weekday
    total_shirts_per_week = total_shirts_per_day * 5 + 3 * 2 + 2  # Kendra wears a different shirt for after-school clubs 3 days a week, wears one shirt all day on Saturday, and wears two different shirts on Sunday

    # Calculate the total number of shirts Kendra needs for two weeks
    total_shirts = total_shirts_per_week * 2

    result = total_shirts
    return result

print(solution())