def solution():
    minutes_per_episode = 20
    filming_time_per_episode = minutes_per_episode * 1.5
    episodes_per_week = 5
    weeks_to_film = 4
    total_filming_time = filming_time_per_episode * episodes_per_week * weeks_to_film
    result = total_filming_time
    return result

print(solution())