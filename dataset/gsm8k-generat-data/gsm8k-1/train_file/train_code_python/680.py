def solution():
    """Fernanda purchased six audiobooks from Audible to listen to from her audible app. If each audiobook was 30 hours long and she listened to 2 hours of an audiobook each day, calculate the total time it took her to finish the six audiobooks?"""
    num_audiobooks = 6
    length_audiobook = 30
    hours_listened_per_day = 2
    total_hours_listened = num_audiobooks * length_audiobook
    num_days_to_finish = total_hours_listened / hours_listened_per_day
    result = num_days_to_finish
    return result

print(solution())