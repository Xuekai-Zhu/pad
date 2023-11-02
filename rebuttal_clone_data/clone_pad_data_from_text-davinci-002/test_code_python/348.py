def solution():
    initial_time = 10
    time_after_first_week = initial_time * 2
    time_after_second_week = time_after_first_week * 2
    time_after_third_week = time_after_second_week + (time_after_second_week / 2)
    result = time_after_third_week
    return result

print(solution())