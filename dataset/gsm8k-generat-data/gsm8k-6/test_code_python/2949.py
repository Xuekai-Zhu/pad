def solution():
    # Calculate the total bathroom time used by the family
    total_bathroom_time = 45 + 30 + 20  # in minutes

    # Calculate the time left for Mrs. Parker to use the bathroom
    time_left = (5*60 - (2*60 + 30)) - total_bathroom_time  # convert 5 pm to minutes and subtract the time spent by the family
    result = time_left  # in minutes
    return result

print(solution())