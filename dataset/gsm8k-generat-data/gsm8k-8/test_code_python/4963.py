def solution():
    # Define the costs for the first and subsequent seasons
    first_season_cost = 100000 * 12
    subsequent_season_cost = first_season_cost * 2
    
    # Calculate the number of episodes in each season
    season1_episodes = 12
    season2_episodes = int(season1_episodes * 1.5)
    season3_episodes = int(season2_episodes * 1.5)
    season4_episodes = int(season3_episodes * 1.5)
    season5_episodes = 24
    
    # Calculate the total cost for each season
    season1_total_cost = first_season_cost
    season2_total_cost = subsequent_season_cost * season2_episodes
    season3_total_cost = subsequent_season_cost * season3_episodes
    season4_total_cost = subsequent_season_cost * season4_episodes
    season5_total_cost = subsequent_season_cost * season5_episodes
    
    # Calculate the total cost for all seasons
    total_cost = season1_total_cost + season2_total_cost + season3_total_cost + season4_total_cost + season5_total_cost
    result = total_cost
    return result

print(solution())