def solution():
    """A TV show costs $100,000 per episode for the first season and twice that much for every other season. The first season had 12 episodes, and every season after that had 50% more episodes except the last season, which had 24 episodes. The show had 5 seasons. How much did it cost to produce all the episodes?"""
    
    # Define the cost of episodes in the first season, and the number of episodes in each season
    first_season_cost = 100000
    first_season_episodes = 12
    
    # Initialize the total cost of all episodes
    total_cost = 0
    
    # Add the cost of episodes in the first season to the total cost
    total_cost += first_season_cost * first_season_episodes
    
    # Loop through the remaining seasons and add the cost of their episodes to the total cost
    for i in range(2, 6):
        # Define the number of episodes in the current season
        if i == 5:
            current_season_episodes = 24
        else:
            current_season_episodes = first_season_episodes * (1.5 ** (i-2))
            
        # Define the cost of episodes in the current season
        current_season_cost = first_season_cost * (2 ** (i-1))
        
        # Add the cost of episodes in the current season to the total cost
        total_cost += current_season_cost * current_season_episodes
    
    # Return the total cost of all episodes
    return total_cost

print(solution())