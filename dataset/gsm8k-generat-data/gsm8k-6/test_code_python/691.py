def solution():
    # Calculate the time difference between New York and Cape Town in hours
    time_difference = 6  # Cape Town is 6 hours ahead of New York

    # Calculate the time Chance spent traveling from New York to Cape Town
    total_time = (10 - 6) + 24  # Chance arrived in Cape Town 10:00 a.m on Tuesday which New York at that time it was 6 a.m. of the same day. Thus, the flight took 24 hours
    result = total_time - time_difference
    return result

print(solution())