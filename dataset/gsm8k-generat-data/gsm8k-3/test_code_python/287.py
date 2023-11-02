def solution():
    """John wants to finish a show in 5 days.  There are 20 episodes and they are each 30 minutes long.  How many hours does he have to watch a day?"""
    # Define the total number of episodes and the length of each episode
    NUM_EPISODES = 20
    EPISODE_LENGTH = 30 # in minutes

    # Calculate the total length of time needed to watch all episodes
    total_length = NUM_EPISODES * EPISODE_LENGTH # in minutes

    # Convert the total length to hours
    total_hours = total_length / 60

    # Calculate the number of hours John needs to watch per day to finish in 5 days
    hours_per_day = total_hours / 5

    # Display the number of hours John needs to watch per day
    result = hours_per_day
    return result

print(solution())