def solution():
    # Calculate the time taken to push the car back to town
    time1 = 3/6  # time taken to cover first 3 miles with a speed of 6 mph
    time2 = 3/3  # time taken to cover next 3 miles with a speed of 3 mph
    time3 = 4/8  # time taken to cover last 4 miles with a speed of 8 mph
    total_time = time1 + time2 + time3  # total time taken to push the car back to town
    result = total_time
    return result

print(solution())