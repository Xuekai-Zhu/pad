def solution():
    """Bob is tilling a plot of his garden. The plot is 110 feet wide by 120 feet long. His tiller digs a swath two feet wide, and he can till 1 foot of ground in about 2 seconds. How long will it take him to till this plot of land, in minutes?"""
    # Define the dimensions of the plot
    width = 110
    length = 120

    # Define the width of the tiller and the time to till 1 foot
    tiller_width = 2
    time_per_foot = 2

    # Calculate the area of each tilled strip
    strip_area = tiller_width * length

    # Calculate the number of strips needed to cross the width of the plot
    num_strips = width / tiller_width

    # Calculate the total area to be tilled
    total_area = width * length

    # Calculate the total time to till the plot
    total_time = num_strips * strip_area * time_per_foot

    # Convert the time from seconds to minutes
    total_time = total_time / 60

    # Return the result
    result = total_time
    return result

print(solution())