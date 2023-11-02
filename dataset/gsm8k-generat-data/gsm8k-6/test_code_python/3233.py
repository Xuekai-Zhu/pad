def solution():
    # Calculate the average percentage of popped kernels in the three bags
    bag1_percent = (60/75) * 100
    bag2_percent = (42/50) * 100
    bag3_percent = (82/100) * 100
    average_percent = (bag1_percent + bag2_percent + bag3_percent) / 3

    result = average_percent
    return result

print(solution())