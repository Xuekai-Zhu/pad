def solution():
    # Define the study times for each day in hours
    day1_time = 2
    day2_time = 2 * day1_time
    day3_time = day2_time - 1

    # Convert study times to minutes and calculate total study time
    total_time = (day1_time * 60) + (day2_time * 60) + (day3_time * 60)
    result = total_time
    return result

print(solution())