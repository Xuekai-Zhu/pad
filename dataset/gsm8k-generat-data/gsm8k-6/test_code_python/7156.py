def solution():
    # Calculate the total time in minutes that Rich took to run the marathon
    total_time = 3 * 60 + 36  # convert 3 hours and 36 minutes to minutes

    # Calculate the average time in minutes per mile
    time_per_mile = total_time / 24

    result = time_per_mile
    return result

print(solution())