def solution():
    """It starts raining at 7:00 and pours heavily until its stops at 17:00 on a particular day. On the second day, the rain takes 2 more hours than it took on the first day to stop. On the third day, the rain pours for twice the amount of time it took on the second day. Calculate the total time it was raining in the three days."""
    first_day_time = 10
    second_day_time = first_day_time + 2
    third_day_time = second_day_time * 2
    total_time = first_day_time + second_day_time + third_day_time
    result = total_time
    return result

print(solution())