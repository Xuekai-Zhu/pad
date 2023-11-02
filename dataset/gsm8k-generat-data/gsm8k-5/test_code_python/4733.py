def solution():
    # Total number of episodes Joe needs to watch
    total_episodes = 4 * 15 + 15  # 4 full seasons and 1 upcoming season

    # Number of days Joe has to watch all episodes
    num_days = 10

    # Calculate the number of episodes Joe needs to watch per day
    episodes_per_day = total_episodes / num_days
    result = episodes_per_day
    return result

print(solution())