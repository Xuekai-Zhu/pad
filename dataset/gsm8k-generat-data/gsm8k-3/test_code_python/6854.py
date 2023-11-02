def solution():
    """A TV show has been going on for 14 years. Out of those 14 years, 8 seasons had 15 episodes, 4 seasons had 20 episodes, and 2 seasons had 12 episodes. What is the average number of episodes per year?"""
    # Define the number of episodes per season for each season type
    EPISODES_15 = 15
    EPISODES_20 = 20
    EPISODES_12 = 12

    # Define the number of seasons for each season type
    SEASONS_15 = 8
    SEASONS_20 = 4
    SEASONS_12 = 2

    # Calculate the total number of episodes
    total_episodes = (EPISODES_15 * SEASONS_15) + (EPISODES_20 * SEASONS_20) + (EPISODES_12 * SEASONS_12)

    # Calculate the average number of episodes per year
    average_episodes_per_year = total_episodes / 14

    # Display the average number of episodes per year
    result = average_episodes_per_year
    return result

print(solution())