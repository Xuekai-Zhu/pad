def solution():
    """Audrey was asleep for 10 hours last night and dreamed for 2/5 of the time. How much of the night was she not dreaming?"""
    sleep_time = 10
    dream_time_ratio = 2/5
    dream_time = sleep_time * dream_time_ratio
    not_dream_time = sleep_time - dream_time
    result = not_dream_time
    return result

print(solution())