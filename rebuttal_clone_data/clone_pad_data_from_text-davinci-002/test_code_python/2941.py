def solution():
    days_driven_per_week = 4
    days_not_driven_per_week = 3
    total_days_driven_in_4_weeks = days_driven_per_week * 4
    total_days_not_driven_in_4_weeks = days_not_driven_per_week * 4
    total_days_driven_in_4_weeks = total_days_driven_in_4_weeks + total_days_not_driven_in_4_weeks
    kilometers_driven_per_day = 140
    total_kilometers_driven_in_4_weeks = kilometers_driven_per_day * total_days_driven_in_4_weeks
    result = total_kilometers_driven_in_4_weeks
    return result

print(solution())