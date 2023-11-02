def solution():
    distance = 448
    time_diff = 0.5 # 30 minutes = 0.5 hours

    # Calculate the speed of the first spacecraft
    speed_1 = distance / 0.5 # traveled in 30 minutes

    # Calculate the speed of the second spacecraft
    speed_2 = distance / (0.5 + time_diff) # traveled in 30 minutes + 30 minute delay

    # Calculate the difference in speed
    speed_diff = abs(speed_1 - speed_2)
    result = speed_diff
    return result

print(solution())