def solution():
    """Hadassah took six hours to paint 12 paintings. What would be the total time she's taken to finish all the paintings if she paints 20 more paintings?"""
    # Define the number of paintings and the time taken to paint them
    paintings = 12
    time = 6

    # Define the additional paintings
    additional_paintings = 20

    # Calculate the time to paint one painting
    time_per_painting = time / paintings

    # Calculate the total time to paint all paintings
    total_time = time_per_painting * (paintings + additional_paintings)

    result = total_time
    return result

print(solution())