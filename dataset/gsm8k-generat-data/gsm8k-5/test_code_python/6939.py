def solution():
    seasons_before_announcement = 9  # There were 9 seasons before the announcement
    regular_season_length = 22  # Each regular season is 22 episodes long
    last_season_length = regular_season_length + 4  # The last season is 4 episodes longer than regular seasons
    total_episodes = seasons_before_announcement * regular_season_length + last_season_length  # Total number of episodes

    # Calculate the total time to watch all episodes
    total_time = total_episodes * 0.5  # Each episode is 0.5 hours long

    result = total_time
    return result

print(solution())