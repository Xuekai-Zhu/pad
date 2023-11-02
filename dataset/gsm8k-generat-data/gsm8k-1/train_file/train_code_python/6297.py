def solution():
    """Marc bought 50 episodes of the show "Friends" online. Each day Marc watches 1/10 of the episodes he bought. How many days will Marc need to finish 50 episodes of the show he bought?"""
    total_episodes = 50
    episodes_watched_per_day = total_episodes * (1/10)
    days_to_finish = total_episodes / episodes_watched_per_day
    result = days_to_finish
    return result

print(solution())