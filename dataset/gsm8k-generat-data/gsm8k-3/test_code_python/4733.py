def solution():
    """Joe found a new series to watch with a final season that will premiere in 10 days. The series has 4 full seasons already aired; each season has 15 episodes. To catch up with the season premiere he has to watch all episodes. How many episodes per day does Joe have to watch?"""
    # Define the number of episodes in each season
    EPISODES_PER_SEASON = 15

    # Define the number of days Joe has to watch all episodes
    DAYS_TO_WATCH = 10

    # Calculate the total number of episodes to watch
    total_episodes = 4 * EPISODES_PER_SEASON

    # Calculate the number of episodes per day Joe has to watch
    episodes_per_day = total_episodes / DAYS_TO_WATCH

    # Display the number of episodes per day
    result = episodes_per_day
    return result

print(solution())