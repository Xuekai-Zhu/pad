def solution():
    """John wants to finish a show in 5 days. There are 20 episodes and they are each 30 minutes long. How many hours does he have to watch a day?"""
    episodes = 20
    minutes_per_episode = 30
    days = 5
    minutes_in_day = 24 * 60
    total_minutes = episodes * minutes_per_episode
    total_hours = total_minutes / minutes_in_day
    hours_per_day = total_hours / days
    result = hours_per_day
    return result

print(solution())