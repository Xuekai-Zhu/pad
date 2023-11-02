def solution():
    """Marc bought 50 episodes of the show "Friends" online. Each day Marc watches 1/10 of the episodes he bought. How many days will Marc need to finish 50 episodes of the show he bought?"""
    # Define the number of episodes Marc bought and the fraction he watches each day
    num_episodes = 50
    fraction_watched_per_day = 1/10

    # Calculate the number of days it will take Marc to finish all the episodes
    num_days = num_episodes / (num_episodes * fraction_watched_per_day)

    # Display the number of days
    result = num_days
    return result

print(solution())