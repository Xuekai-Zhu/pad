def solution():
    """There are 480 zombies in the shopping mall. If the number of zombies doubled every day, how many days ago were there less than 50 zombies in the mall?"""
    # Define the initial number of zombies and the minimum number of zombies
    starting_zombies = 480
    min_zombies = 50

    # Initialize the day counter
    day = 0

    # Keep dividing by 2 and incrementing the day counter until the number of zombies is less than the minimum
    while starting_zombies >= min_zombies:
        starting_zombies /= 2
        day += 1

    result = day
    return result

print(solution())