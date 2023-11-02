def solution():
    # Calculate the total number of episodes in the 9 seasons
    total_episodes = 9 * 22

    # Calculate the total number of episodes in the last season
    last_season_episodes = total_episodes + 4

    # Calculate the total number of hours to watch all the episodes
    total_hours = (total_episodes + last_season_episodes) * 0.5

    result = total_hours
    return result

print(solution())