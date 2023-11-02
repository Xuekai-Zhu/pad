def solution():
    # time in minutes for each mile
    mile1_time = 6
    mile2_time = 5
    mile3_time = 5
    mile4_time = 4
    
    # calculate the total time for all 4 miles
    total_time = mile1_time + (2 * mile2_time) + mile4_time
    
    # calculate the average time per mile
    average_time_per_mile = total_time / 4
    result = average_time_per_mile
    return result

print(solution())