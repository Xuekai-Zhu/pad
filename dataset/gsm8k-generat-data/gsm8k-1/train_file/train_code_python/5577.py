def solution():
    """Willy is starting a new TV series on Netflix. The TV series has 3 seasons that are each 20 episodes long. If Willy watches 2 episodes a day, how many days will it take for Willy to finish the entire series?"""
    episodes_per_season = 20
    total_episodes = episodes_per_season * 3
    episodes_watched_per_day = 2
    days_to_finish = total_episodes / episodes_watched_per_day
    result = days_to_finish
    return result

print(solution())