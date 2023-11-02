def solution():
    cups_last_week = 20
    percent_increase = 0.30
    cups_this_week = cups_last_week + (cups_last_week * percent_increase)

    total_cups = cups_last_week + cups_this_week
    result = total_cups
    return result

print(solution())