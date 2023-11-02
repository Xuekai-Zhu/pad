def solution():
    """Tim host a show and they film multiple episodes per day. Each episode is 20 minutes long and it takes 50% longer than that to film each episode. Each week they show 5 episodes. How many hours would it take to film 4 weeks of episodes?"""
    episode_length = 20
    filming_time_multiplier = 1.5
    filming_length = episode_length * filming_time_multiplier
    episodes_per_week = 5
    weeks = 4
    total_filming_time = filming_length * episodes_per_week * weeks / 60
    result = total_filming_time
    return result

print(solution())