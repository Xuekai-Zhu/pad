def solution():
    # Calculate the area of the plot of land
    area = 110 * 120

    # Calculate the length of each pass of the tiller
    pass_length = 118  # subtracting 2 feet for the width of the tiller

    # Calculate the time it takes to till 1 square foot of ground
    time_per_square_foot = 2  # 1 foot of ground in 2 seconds

    # Calculate the time it takes to till the entire plot of land in seconds
    time_in_seconds = area * pass_length * time_per_square_foot

    # Convert the time to minutes
    time_in_minutes = time_in_seconds / 60

    result = time_in_minutes
    return result

print(solution())