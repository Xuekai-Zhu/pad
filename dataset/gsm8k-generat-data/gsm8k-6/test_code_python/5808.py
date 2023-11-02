def solution():
    # Convert 8 hours to minutes
    total_time = 8 * 60

    # Calculate the time Lilly spent cleaning (a quarter of the total time)
    lilly_time = total_time/4

    # Calculate the time Fiona spent cleaning (the remaining three quarters of the total time)
    fiona_time = 3*lilly_time

    # Return the time Fiona spent cleaning in minutes
    result = fiona_time
    return result

print(solution())