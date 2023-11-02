def solution():
    """Corey downloaded two movie series from his Netflix account 
    with 12 and 14 seasons per series, respectively. However, in the week, 
    his computer got a mechanical failure, and he lost two episodes from each 
    season for both series. If each season in the movie series that Corey 
    downloaded had 16 episodes, how many episodes remained after the computer's 
    mechanical failure?"""
    
    series1_seasons = 12
    series2_seasons = 14
    episodes_per_season = 16
    episodes_lost_per_season = 2
    
    total_episodes = (series1_seasons + series2_seasons) * episodes_per_season
    total_episodes_lost = (series1_seasons + series2_seasons) * episodes_lost_per_season
    episodes_remaining = total_episodes - total_episodes_lost
    
    result = episodes_remaining
    return result

print(solution())