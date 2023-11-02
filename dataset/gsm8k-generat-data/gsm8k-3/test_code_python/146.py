def solution():
    """Richard can clean his room in 22 minutes. Cory takes 3 minutes more than Richard to clean her room while Blake can clean his room 4 minutes more quickly than Cory. If they have to clean their rooms twice a week, how many minutes do all three spend cleaning their rooms each week?"""
    # Define the time taken by Richard to clean his room
    richard_time = 22

    # Define the time taken by Cory to clean her room
    cory_time = richard_time + 3

    # Define the time taken by Blake to clean his room
    blake_time = cory_time - 4

    # Calculate the total time taken by all three to clean their rooms in a week
    total_time = 2 * (richard_time + cory_time + blake_time)

    # return the result
    result = total_time
    return result

print(solution())