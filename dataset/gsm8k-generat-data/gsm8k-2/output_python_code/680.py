def solution():
    """Fernanda purchased six audiobooks from Audible to listen to from her audible app. If each audiobook was 30 hours long and she listened to 2 hours of an audiobook each day, calculate the total time it took her to finish the six audiobooks?"""
    audiobook_length = 30
    daily_listening_time = 2
    total_listening_time = audiobook_length * 6
    days_to_finish = total_listening_time / daily_listening_time
    result = days_to_finish
    return result

print(solution())