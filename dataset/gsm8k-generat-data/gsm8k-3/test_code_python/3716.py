def solution():
    """John starts at an elevation of 400 feet.  He travels downward at a rate of 10 feet down per minute for 5 minutes.  What is his elevation now?"""
    # Define John's starting elevation
    starting_elevation = 400

    # Define the rate of descent per minute
    rate_of_descent = 10

    # Define the time spent descending in minutes
    time_descending = 5

    # Calculate John's new elevation
    new_elevation = starting_elevation - (rate_of_descent * time_descending)

    # Display John's new elevation
    result = new_elevation
    return result

print(solution())