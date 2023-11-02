def solution():
    # Calculate the total time Jack took to run up the hill
    total_time_Jack = 19 + (32 + 7)/2  # Jack ran up the first half of the hill in 19 seconds and finished 7 seconds before Jill who finished in 32 seconds

    # Calculate the time it took Jack to run up the second half of the hill
    time_Jack_second_half = total_time_Jack - 19  # time taken to run first half subtracted from total time taken 
    result = time_Jack_second_half
    return result

print(solution())