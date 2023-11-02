def solution():
    # Calculate the total number of episodes Joe needs to watch
    total_episodes = 4 * 15  # 4 full seasons, each with 15 episodes
    days_left = 10  # number of days left until the season premiere
    episodes_per_day = total_episodes / days_left  # calculate episodes per day
    result = episodes_per_day
    return result

print(solution())