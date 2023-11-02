def solution():
    """Tom is binge-watching a show on Netflix. The show has 90 episodes, each one of which is 20 minutes long because there are no commercials. If Tom can spend two hours a day watching the show, how many days will it take him to finish watching the show?"""
    # Define the number of episodes and the length of each episode
    NUM_EPISODES = 90
    EPISODE_LENGTH = 20

    # Define Tom's daily watching time in minutes
    DAILY_WATCH_TIME = 120

    # Calculate the total time needed to watch all the episodes
    total_time = NUM_EPISODES * EPISODE_LENGTH

    # Calculate the number of days needed to watch all the episodes
    num_days = total_time // DAILY_WATCH_TIME + 1

    # Display the number of days needed to watch all the episodes
    result = num_days
    return result

print(solution())