def solution():
    width = 110  # Width of the plot of land in feet
    length = 120  # Length of the plot of land in feet
    swath_width = 2  # Width of the tiller's swath in feet
    tilling_speed = 0.5  # The tiller can till 1 foot of ground in 2 seconds (0.5 feet per second)

    # Calculate the total area of the plot of land
    area = width * length

    # Calculate the total length of the tiller's path
    path_length = 2 * length + 2 * (width - swath_width)

    # Calculate the total time it will take for Bob to till the plot of land
    total_time = path_length * tilling_speed

    # Convert the time to minutes
    total_time_minutes = total_time / 60

    result = total_time_minutes
    return result

print(solution())