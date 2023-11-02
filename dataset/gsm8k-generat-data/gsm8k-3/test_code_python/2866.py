def solution():
    """Erin is watching a TV mini series of Pride and Prejudice. There are 6 episodes that are each 50 minutes long. If Erin watches all of the episodes in one sitting, one after the other with no breaks, how many hours will she spend watching the series?"""
    # Define the length of each episode in minutes
    EPISODE_LENGTH = 50

    # Define the number of episodes
    NUM_EPISODES = 6

    # Calculate the total length of the mini series in minutes
    total_length_in_minutes = EPISODE_LENGTH * NUM_EPISODES

    # Convert the total length to hours
    total_length_in_hours = total_length_in_minutes / 60

    # Display the total length in hours
    result = total_length_in_hours
    return result

print(solution())