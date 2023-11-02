def solution():
    """John wants to finish a show in 5 days. There are 20 episodes and they are each 30 minutes long. How many hours does he have to watch a day?"""
    total_episodes = 20
    episode_length = 30 # in minutes
    total_minutes = total_episodes * episode_length
    minutes_per_day = total_minutes / 5
    hours_per_day = minutes_per_day / 60
    result = hours_per_day
    return result

print(solution())