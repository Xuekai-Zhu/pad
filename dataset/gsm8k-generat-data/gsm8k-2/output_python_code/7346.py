def solution():
    """Tim watches 2 shows. One of them is a half-hour show per episode and the other is a 1-hour long show per episode. The short show had 24 episodes and the long show had 12 episodes. How many hours of TV did he watch?"""
    short_show_time = 0.5
    long_show_time = 1
    short_show_episodes = 24
    long_show_episodes = 12
    total_time = short_show_time * short_show_episodes + long_show_time * long_show_episodes
    result = total_time
    return result

print(solution())