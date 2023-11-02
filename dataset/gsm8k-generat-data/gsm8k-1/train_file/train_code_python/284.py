def solution():
    """John wants to finish a show in 5 days. There are 20 episodes and they are each 30 minutes long. How many hours does he have to watch a day?"""
    total_episodes = 20
    episode_length = 30  # in minutes
    num_days = 5
    total_time = total_episodes * episode_length  # in minutes
    hours_per_day = total_time / (num_days * 60)  # in hours
    result = hours_per_day
    return result

print(solution())