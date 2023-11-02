def solution():
    """A TV show costs $100,000 per episode for the first season and twice that much for every other season. The first season had 12 episodes, and every season after that had 50% more episodes except the last season, which had 24 episodes. The show had 5 seasons. How much did it cost to produce all the episodes?"""
    first_season_cost = 100000 * 12
    
    total_seasons = 5
    
    total_cost = first_season_cost
    
    for season in range(2, total_seasons+1):
        # 50% increase in number of episodes except for last season
        if season != total_seasons:
            num_episodes = int(12 * 1.5)
        else:
            num_episodes = 24
            
        cost_per_episode = 100000 * 2**(season-1)
        total_cost += num_episodes * cost_per_episode
    
    result = total_cost
    return result

print(solution())