def solution():
    audiobooks = 6
    hours_per_audiobook = 30
    hours_listened_per_day = 2
    total_hours = audiobooks * hours_per_audiobook
    total_days = total_hours / hours_listened_per_day
    result = total_days
    return result

print(solution())