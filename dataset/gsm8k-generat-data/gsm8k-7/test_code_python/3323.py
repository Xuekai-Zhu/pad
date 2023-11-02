def solution():
    # Calculate the time it took to push the car for the first three miles
    time1 = 3 / 6  # 3 miles at 6 miles per hour

    # Calculate the time it took to push the car for the next three miles
    time2 = 3 / 3  # 3 miles at 3 miles per hour

    # Calculate the time it took to push the car for the last four miles
    time3 = 4 / 8  # 4 miles at 8 miles per hour

    # Calculate the total time it took to push the car back to town
    total_time = time1 + time2 + time3
    result = total_time
    return result

print(solution())