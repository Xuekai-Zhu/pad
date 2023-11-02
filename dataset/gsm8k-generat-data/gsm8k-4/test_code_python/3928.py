def solution():
    """If it takes 20 minutes to paint a house, how many houses can you paint in 3 hours?"""
    # Define the time it takes to paint one house and the total painting time
    time_per_house = 20   # minutes
    total_time = 3*60    # minutes

    # Calculate the number of houses that can be painted in the total time
    num_houses = total_time // time_per_house

    # return the result
    result = num_houses
    return result

print(solution())