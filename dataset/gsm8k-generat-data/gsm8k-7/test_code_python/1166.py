def solution():
    num_cricket_first_day = 0.3 * 70
    num_cricket_second_day = num_cricket_first_day - 6
    num_cricket_third_day = 70 - (num_cricket_first_day + num_cricket_second_day)
    result = num_cricket_third_day
    return result

print(solution())