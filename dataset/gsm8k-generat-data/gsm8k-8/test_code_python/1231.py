def solution():
    # Define the distance and time for the first spacecraft
    d1 = 448
    t1 = 0.5

    # Calculate the speed for the first spacecraft
    s1 = d1 / t1

    # Define the distance and time for the second spacecraft
    d2 = 448
    t2 = 0.5 + 0.5

    # Calculate the speed for the second spacecraft
    s2 = d2 / t2

    # Calculate the difference in speed
    speed_difference = s2 - s1
    result = speed_difference
    return result

print(solution())