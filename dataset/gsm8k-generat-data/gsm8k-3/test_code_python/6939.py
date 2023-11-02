def solution():
    """John watches a TV show and they announce they are going to do 1 more season.  Each season is 22 episodes except for the last season which is 4 episodes longer.  There were 9 seasons before the announcement.  If each episode is .5 hours how long will it take to watch them all after the last season finishes?"""
    # Define the number of episodes per season
    EPISODES_PER_SEASON = 22

    # Define the number of episodes in the last season
    LAST_SEASON_EPISODES = 26

    # Define the number of seasons before the announcement
    SEASONS_BEFORE_ANNOUNCEMENT = 9

    # Calculate the total number of episodes
    total_episodes = (SEASONS_BEFORE_ANNOUNCEMENT * EPISODES_PER_SEASON) + LAST_SEASON_EPISODES

    # Calculate the total watch time in hours
    total_watch_time = total_episodes * 0.5

    # Display the total watch time
    result = total_watch_time
    return result

print(solution())