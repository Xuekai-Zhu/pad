def solution():
    """Erin is watching a TV mini series of Pride and Prejudice. There are 6 episodes that are each 50 minutes long. If Erin watches all of the episodes in one sitting, one after the other with no breaks, how many hours will she spend watching the series?"""
    # Define the length of each episode in minutes and the number of episodes
    EPISODE_LENGTH = 50
    NUM_EPISODES = 6

    # Calculate the total length of the series in minutes
    total_minutes = EPISODE_LENGTH * NUM_EPISODES

    # Calculate the total length of the series in hours
    total_hours = total_minutes / 60

    # Return the result
    result = total_hours
    return result

print(solution())