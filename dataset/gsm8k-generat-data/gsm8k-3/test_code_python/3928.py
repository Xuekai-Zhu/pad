def solution():
    """If it takes 20 minutes to paint a house, how many houses can you paint in 3 hours?"""
    # Define the time it takes to paint one house in minutes
    TIME_PER_HOUSE = 20

    # Convert 3 hours to minutes
    total_time = 3 * 60

    # Calculate the number of houses that can be painted in 3 hours
    num_houses = total_time // TIME_PER_HOUSE

    # Display the number of houses that can be painted
    result = num_houses
    return result

print(solution())