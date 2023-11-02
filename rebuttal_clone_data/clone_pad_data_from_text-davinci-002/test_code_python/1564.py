def solution():
     minutes_watched_Monday = 138
     minutes_watched_Thursday = 21
     minutes_per_episode = 44
     episodes_watched_Friday = 2
     total_minutes_watched = minutes_watched_Monday + (minutes_per_episode * episodes_watched_Friday) + minutes_watched_Thursday
     result = total_minutes_watched
     return result

print(solution())