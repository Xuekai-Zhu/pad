def solution():
    # Calculate the total time for each load of laundry
    whites_time = 72 + 50
    darks_time = 58 + 65
    colors_time = 45 + 54

    # Calculate the total time to do all three loads, one at a time
    total_time = whites_time + darks_time + colors_time
    result = total_time
    return result

print(solution())