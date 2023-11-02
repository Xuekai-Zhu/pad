def solution():
    # Total time it rained on the first day
    day1_time = 10  # 7:00 to 17:00 is 10 hours

    # Total time it rained on the second day
    day2_time = day1_time + 2  # The rain took 2 more hours to stop on the second day

    # Total time it rained on the third day
    day3_time = day2_time * 2  # The rain poured for twice the time on the third day

    # Total time it was raining in the three days
    total_time = day1_time + day2_time + day3_time
    result = total_time
    return result

print(solution())