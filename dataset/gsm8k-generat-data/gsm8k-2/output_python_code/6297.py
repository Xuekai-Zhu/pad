def solution():
    """Marc bought 50 episodes of the show "Friends" online. Each day Marc watches 1/10 of the episodes he bought. How many days will Marc need to finish 50 episodes of the show he bought?"""
    total_episodes = 50
    daily_watching = total_episodes / 10
    days_needed = total_episodes / daily_watching
    result = days_needed
    return result

print(solution())