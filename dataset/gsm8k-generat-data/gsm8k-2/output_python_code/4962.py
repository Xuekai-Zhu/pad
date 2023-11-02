def solution():
    """A TV show costs $100,000 per episode for the first season and twice that much for every other season. The first season had 12 episodes, and every season after that had 50% more episodes except the last season, which had 24 episodes. The show had 5 seasons. How much did it cost to produce all the episodes?"""
    first_season_cost = 100000 * 12
    total_cost = first_season_cost
    cost_per_episode = 200000
    num_episodes = 12
    for i in range(2, 6):
        if i == 5:
            num_episodes = 24
        else:
            num_episodes = int(num_episodes * 1.5)
        total_cost += cost_per_episode * num_episodes

    result = total_cost
    return result

print(solution())