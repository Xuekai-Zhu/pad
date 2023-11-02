def solution():
    # Calculate the total number of episodes
    total_episodes = 4 * 15

    # Calculate the number of days Joe has to watch all episodes
    days_to_watch = 10

    # Calculate the number of episodes per day
    episodes_per_day = total_episodes / days_to_watch
    result = episodes_per_day
    return result

print(solution())