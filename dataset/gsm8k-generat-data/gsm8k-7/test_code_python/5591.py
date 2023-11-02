def solution():
    current_time = 30
    extra_time_per_day = 10
    days = 3

    while current_time < 90:
        current_time += extra_time_per_day
        days += 1

    result = days
    return result

print(solution())