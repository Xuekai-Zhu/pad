def solution():
    """Joe found a new series to watch with a final season that will premiere in 10 days. The series has 4 full seasons already aired; each season has 15 episodes. To catch up with the season premiere he has to watch all episodes. How many episodes per day does Joe have to watch?"""
    total_episodes = 4 * 15
    days_to_watch = 10
    episodes_per_day = total_episodes / days_to_watch
    result = episodes_per_day
    return result

print(solution())