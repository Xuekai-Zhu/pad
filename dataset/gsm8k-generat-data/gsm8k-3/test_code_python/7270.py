def solution():
    """Bob is tilling a plot of his garden. The plot is 110 feet wide by 120 feet long. His tiller digs a swath two feet wide, and he can till 1 foot of ground in about 2 seconds. How long will it take him to till this plot of land, in minutes?"""
    # Calculate the total area of the plot
    plot_area = 110 * 120

    # Calculate the area that Bob can till in one pass
    pass_area = 2 * 120

    # Calculate the number of passes Bob needs to make
    num_passes = int((plot_area + pass_area - 1) / pass_area)

    # Calculate the total time it will take Bob to till the plot
    time_in_seconds = num_passes * pass_area * 2
    time_in_minutes = time_in_seconds / 60

    # Display the time it will take Bob to till the plot
    result = time_in_minutes
    return result

print(solution())