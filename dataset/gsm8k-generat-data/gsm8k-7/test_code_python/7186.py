def solution():
    num_5minute_commercials = 3
    num_2minute_commercials = 11

    # Calculate the total time for the 5-minute commercials
    total_5minute_time = num_5minute_commercials * 5

    # Calculate the total time for the 2-minute commercials
    total_2minute_time = num_2minute_commercials * 2

    # Calculate the total time for the commercial break
    total_time = total_5minute_time + total_2minute_time
    result = total_time
    return result

print(solution())