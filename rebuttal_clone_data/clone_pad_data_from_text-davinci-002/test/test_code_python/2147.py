def solution():
    hours_slept_per_day = 4
    recommended_hours_slept_per_day = 6
    hours_lacking_per_day = recommended_hours_slept_per_day - hours_slept_per_day
    hours_lacking_per_week = hours_lacking_per_day * 7
    result = hours_lacking_per_week
    return result

print(solution())