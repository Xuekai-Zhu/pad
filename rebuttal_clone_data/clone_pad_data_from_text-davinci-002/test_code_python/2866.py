def solution():
    episodes = 6
    minutes_per_episode = 50
    minutes_in_an_hour = 60
    total_minutes = episodes * minutes_per_episode
    total_hours = total_minutes / minutes_in_an_hour
    result = total_hours
    return result

print(solution())