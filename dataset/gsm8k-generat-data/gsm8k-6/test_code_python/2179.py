def solution():
    # Calculate the total length of the podcasts
    total_length = (45/60) + (2*45/60) + (1 + 45/60) + 1  # convert minutes to hours
    remaining_time = 6 - total_length  # calculate remaining time in hours
    result = round(remaining_time, 2)  # round the result to 2 decimal places
    return result

print(solution())