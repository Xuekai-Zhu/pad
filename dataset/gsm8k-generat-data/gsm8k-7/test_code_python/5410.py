def solution():
    # Calculate the time it will take James to hike the first trail (20 miles downhill at 5 mph)
    trail1_time = 20 / 5

    # Calculate the time it will take James to hike the second trail (6 miles uphill at 3 mph, 1 hour break, then 6 miles downhill at 5 mph)
    trail2_time = (6 / 3) + 1 + (6 / 5)

    # Calculate the total time for the second trail, including the uphill and downhill portions
    total_trail2_time = trail2_time * 2

    # Calculate the time difference between the two trails
    time_difference = total_trail2_time - trail1_time
    result = time_difference
    return result

print(solution())