def solution():
    """Joe found a new series to watch with a final season that will premiere in 10 days. The series has 4 full seasons already aired; each season has 15 episodes. To catch up with the season premiere he has to watch all episodes. How many episodes per day does Joe have to watch?"""
    # Define the number of full seasons and episodes per season
    full_seasons = 4
    episodes_per_season = 15

    # Calculate the total number of episodes to watch
    total_episodes = full_seasons * episodes_per_season

    # Calculate the number of days to watch all episodes
    days_to_watch = 10

    # Calculate the number of episodes to watch per day
    episodes_per_day = total_episodes / days_to_watch

    # Round up to the nearest whole number
    episodes_per_day = int(round(episodes_per_day, 0))

    # Return the result
    result = episodes_per_day
    return result

print(solution())