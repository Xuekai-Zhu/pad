def solution():
    total_seasons = 12  # The series has 12 seasons
    episodes_per_season = 20  # Each season has 20 episodes
    total_episodes = total_seasons * episodes_per_season  # Total number of episodes in the series
    watched_fraction = 1/3  # Cesar watched 1/3 of the series before the school closed

    # Calculate the number of episodes Cesar already watched
    watched_episodes = round(watched_fraction * total_episodes)

    # Calculate the number of episodes remaining for Cesar to watch
    remaining_episodes = total_episodes - watched_episodes
    result = remaining_episodes
    return result

print(solution())