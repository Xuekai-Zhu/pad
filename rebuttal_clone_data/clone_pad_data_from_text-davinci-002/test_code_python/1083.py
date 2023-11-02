def solution():
    tv_per_day_1 = 10
    reduction_percent = 10
    tv_per_day_2 = tv_per_day_1 - (tv_per_day_1 * (reduction_percent / 100))
    result = tv_per_day_2
    return result

print(solution())