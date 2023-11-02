def solution():
    # Calculate the time Delaney missed his bus by
    missed_time = (8 * 60) - ((7 * 60) + 50 + 30)  # 8:00 a.m is 480 minutes, Delaney left home at 7:50 a.m and it takes 30 minutes to reach the pick-up point
    result = missed_time
    return result

print(solution())