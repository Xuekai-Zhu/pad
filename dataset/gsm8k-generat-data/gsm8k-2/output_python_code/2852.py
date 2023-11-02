def solution():
    """Tim host a show and they film multiple episodes per day. Each episode is 20 minutes long and it takes 50% longer than that to film each episode. Each week they show 5 episodes. How many hours would it take to film 4 weeks of episodes?"""
    time_per_episode = 20
    filming_time_per_episode = time_per_episode * 1.5
    episodes_per_week = 5
    total_filming_time = filming_time_per_episode * episodes_per_week * 4
    total_hours = total_filming_time / 60
    result = total_hours
    return result

print(solution())