def solution():
    shells_per_day = 10
    total_days = 6
    shells_given_to_brother = 2

    total_shells = shells_per_day * total_days
    shells_left = total_shells - shells_given_to_brother
    result = shells_left
    return result

print(solution())