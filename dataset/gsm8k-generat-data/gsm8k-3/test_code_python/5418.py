def solution():
    """There are 480 zombies in the shopping mall. If the number of zombies doubled every day, how many days ago were there less than 50 zombies in the mall?"""
    # Define the initial number of zombies and the threshold number of zombies
    starting_zombies = 480
    threshold_zombies = 50

    # Initialize the number of days
    days = 0

    # Loop until the number of zombies drops below the threshold
    while starting_zombies >= threshold_zombies:
        days += 1
        starting_zombies = starting_zombies / 2

    # Display the number of days
    result = days
    return result

print(solution())