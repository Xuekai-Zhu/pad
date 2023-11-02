def solution():
    """Hadassah took six hours to paint 12 paintings. What would be the total time she's taken to finish all the paintings if she paints 20 more paintings?"""
    # Define the number of paintings and time taken for the first batch
    paintings_1 = 12
    time_1 = 6

    # Define the additional number of paintings
    paintings_2 = 20

    # Calculate the total time to complete all the paintings
    time_2 = (paintings_1 + paintings_2) * (time_1 / paintings_1)

    # Display the total time
    result = time_2
    return result

print(solution())