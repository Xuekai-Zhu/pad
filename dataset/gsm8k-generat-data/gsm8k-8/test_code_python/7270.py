def solution():
    # Calculate the area to be tilled
    area = 110 * 120

    # Calculate the length of each pass of the tiller
    pass_length = 120

    # Calculate the number of passes needed
    passes = pass_length / 2

    # Calculate the time per foot of ground
    time_per_foot = 2

    # Calculate the total time in seconds
    total_time = area * passes * time_per_foot

    # Convert to minutes
    total_time_minutes = total_time / 60
    result = total_time_minutes
    return result

print(solution())