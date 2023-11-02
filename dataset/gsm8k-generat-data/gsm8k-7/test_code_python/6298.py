def solution():
    num_episodes = 50
    fraction_watched_per_day = 1/10

    # Calculate the total number of days it will take Marc to finish all episodes
    total_days = num_episodes * fraction_watched_per_day
    result = total_days
    return result

print(solution())