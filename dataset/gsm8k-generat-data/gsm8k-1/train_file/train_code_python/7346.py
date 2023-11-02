def solution():
    """Tim watches 2 shows. One of them is a half-hour show per episode and the other is a 1-hour long show per episode. The short show had 24 episodes and the long show had 12 episodes. How many hours of TV did he watch?"""
    half_hour_show = 0.5
    one_hour_show = 1
    half_hour_episodes = 24
    one_hour_episodes = 12
    total_hours = (half_hour_show * half_hour_episodes) + (one_hour_show * one_hour_episodes)
    result = total_hours
    return result

print(solution())