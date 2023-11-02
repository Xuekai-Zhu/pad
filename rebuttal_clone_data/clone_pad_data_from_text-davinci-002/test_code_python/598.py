def solution():
    cups_eaten = 8
    days_ so_far = 4
    recommended_cups_per_day = 2
    cups_remaining = (recommended_cups_per_day * 7) - cups_eaten
    cups_per_day_remaining = cups_remaining / 3
    result = cups_per_day_remaining
    return result

print(solution())