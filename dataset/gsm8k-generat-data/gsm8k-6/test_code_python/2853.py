def solution():
    episode_length = 20  # minutes
    filming_time = episode_length * 1.5  # 50% longer than episode length
    episodes_per_week = 5
    weeks = 4
    total_filming_time = episodes_per_week * filming_time * weeks  # in minutes
    total_filming_time_hours = total_filming_time / 60  # convert to hours
    result = total_filming_time_hours
    return result

print(solution())