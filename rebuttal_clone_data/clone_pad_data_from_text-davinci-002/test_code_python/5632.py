def solution():
    episodes = 90
    minutes_per_episode = 20
    hours_per_day = 2
    minutes_per_hour = 60
    minutes_per_day_available = hours_per_day * minutes_per_hour
    minutes_to_binge = episodes * minutes_per_episode
    days_to_binge = minutes_to_binge / minutes_per_day_available
    result = days_to_binge
    return result

print(solution())