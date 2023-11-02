def solution():
    """Jerry is trying to cut down on the amount of soda he drinks. Right now, he drinks 48 sodas a week. If he cuts the number of sodas he drinks in half each week, how many weeks will it take him to only drink 6 sodas per week?"""
    # Define the initial number of sodas Jerry drinks per week
    initial_sodas = 48

    # Define the target number of sodas Jerry wants to drink per week
    target_sodas = 6

    # Initialize the week counter
    weeks = 0

    # Halve the number of sodas each week until the target is reached
    while initial_sodas > target_sodas:
        initial_sodas /= 2
        weeks += 1

    # Return the number of weeks it took to reach the target
    result = weeks
    return result

print(solution())