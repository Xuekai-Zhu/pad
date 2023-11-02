def solution():
    """A TV show costs $100,000 per episode for the first season and twice that much for every other season.  
    The first season had 12 episodes, and every season after that had 50% more episodes except the last season, 
    which had 24 episodes. The show had 5 seasons. How much did it cost to produce all the episodes?"""
    
    # Define the cost per episode for the first season and second season
    first_season_cost = 100000
    second_season_cost = first_season_cost * 2

    # Define the number of episodes in the first season and last season
    first_season_episodes = 12
    last_season_episodes = 24

    # Define the ratio of episodes between seasons except for the last season
    episode_ratio = 1.5

    # Define the number of seasons
    num_seasons = 5

    # Calculate the total number of episodes
    total_episodes = first_season_episodes
    for i in range(1, num_seasons):
        episodes = int(first_season_episodes * (episode_ratio ** i))
        if i == num_seasons-1:
            episodes = last_season_episodes
        total_episodes += episodes

    # Calculate the total cost of all episodes
    total_cost = (first_season_episodes * first_season_cost) + ((total_episodes - first_season_episodes) * second_season_cost)

    # Display the total cost
    result = total_cost
    return result

print(solution())