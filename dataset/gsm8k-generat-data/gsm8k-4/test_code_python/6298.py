def solution():
    """Marc bought 50 episodes of the show "Friends" online. Each day Marc watches 1/10 of the episodes he bought. How many days will Marc need to finish 50 episodes of the show he bought?"""
    # Define the number of episodes Marc bought and the fraction he watches each day
    total_episodes = 50
    fraction_per_day = 1/10

    # Calculate the number of days Marc will need to finish all the episodes
    days = total_episodes / (total_episodes * fraction_per_day)

    # Return the result
    result = days
    return result

print(solution())