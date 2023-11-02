def solution():
    initial_squats = 30
    increase_per_day = 5
    num_days = 4

    total_squats = 0
    for i in range(num_days):
        total_squats += initial_squats + (increase_per_day * i)

    num_squats_day_after_tomorrow = initial_squats + (increase_per_day * 2)
    result = num_squats_day_after_tomorrow
    return result

print(solution())