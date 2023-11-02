def solution():
    total_leaves = 1000
    leaves_lost_first_week = total_leaves * (2/5)
    leaves_remaining = total_leaves - leaves_lost_first_week
    leaves_lost_second_week = leaves_remaining * (4/10)
    leaves_remaining_second_week = leaves_remaining - leaves_lost_second_week
    leaves_lost_third_week = leaves_remaining_second_week * (3/4)
    leaves_remaining_third_week = leaves_remaining_second_week - leaves_lost_third_week
    result = leaves_remaining_third_week
    return result

print(solution())