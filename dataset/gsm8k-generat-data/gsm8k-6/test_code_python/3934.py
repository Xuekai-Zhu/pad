def solution():
    # Calculate the total time spent at the gym on Monday and Wednesday
    monday_wednesday_total = 1.5 * 2

    # Calculate the total time spent at the gym on Tuesday, Wednesday and Friday
    tuesday_friday_total = 5 - monday_wednesday_total

    # Divide the total time spent on Tuesday and Friday equally
    time_per_day = tuesday_friday_total / 2

    result = time_per_day
    return result

print(solution())