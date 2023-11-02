def solution():
    """Tim watches 2 shows. One of them is a half-hour show per episode and the other is a 1-hour long show per episode. The short show had 24 episodes and the long show had 12 episodes. How many hours of TV did he watch?"""
    # Define the length of each episode in hours
    SHORT_EPISODE_LENGTH = 0.5
    LONG_EPISODE_LENGTH = 1

    # Define the number of episodes watched for each show
    short_episodes = 24
    long_episodes = 12

    # Calculate the total time spent watching each show
    short_time = short_episodes * SHORT_EPISODE_LENGTH
    long_time = long_episodes * LONG_EPISODE_LENGTH

    # Calculate the total time spent watching TV
    total_time = short_time + long_time

    # Display the total time
    result = total_time
    return result

print(solution())