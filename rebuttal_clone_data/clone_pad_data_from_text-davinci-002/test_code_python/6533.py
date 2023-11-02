def solution():
    water_yesterday = 48
    percent_decrease = 4
    real_percent_decrease = percent_decrease / 100
    two_days_ago = water_yesterday / (1 - real_percent_decrease)
    result = two_days_ago
    return result

print(solution())