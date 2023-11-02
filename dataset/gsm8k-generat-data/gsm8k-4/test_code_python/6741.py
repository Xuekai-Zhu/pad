def solution():
    """While chatting in the school cafeteria, Cesar's friend Demi tells him that a new fantasy series was on Netflix and he should watch it. The new series has 12 seasons, and each season has 20 episodes. If Cesar watched 1/3 of the series before the school closed, how many episodes were remaining for him to finish the series?"""
    # Define the number of seasons and episodes per season
    seasons = 12
    episodes_per_season = 20

    # Calculate the total number of episodes
    total_episodes = seasons * episodes_per_season

    # Calculate the number of episodes Cesar watched before school closed
    watched_episodes = total_episodes * (1/3)

    # Calculate the number of episodes left to watch
    remaining_episodes = total_episodes - watched_episodes

    result = remaining_episodes
    return result

print(solution())