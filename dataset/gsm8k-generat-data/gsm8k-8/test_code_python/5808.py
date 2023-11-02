def solution():
    # Calculate the total time spent cleaning in hours
    total_time = 8

    # Calculate Lilly's time spent cleaning in hours
    lilly_time = total_time / 4

    # Calculate Fiona's time spent cleaning in hours
    fiona_time = total_time - lilly_time

    # Convert Fiona's time spent cleaning to minutes
    fiona_time_minutes = fiona_time * 60

    result = fiona_time_minutes
    return result

print(solution())