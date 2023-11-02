def solution():
    leaves_per_pound = 1000
    weight_per_day = 100 / leaves_per_pound
    days_until_collapse = 500 / weight_per_day
    result = days_until_collapse
    return result

print(solution())