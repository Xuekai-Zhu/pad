def solution():
    """Willy is starting a new TV series on Netflix. The TV series has 3 seasons that are each 20 episodes long. If Willy watches 2 episodes a day, how many days will it take for Willy to finish the entire series?"""
    num_seasons = 3
    num_episodes = 20
    episodes_per_day = 2
    total_num_episodes = num_seasons * num_episodes
    num_days = total_num_episodes // episodes_per_day
    if total_num_episodes % episodes_per_day != 0:
        num_days += 1
    result = num_days
    return result

print(solution())