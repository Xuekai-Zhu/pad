def solution():
    """Audrey was asleep for 10 hours last night and dreamed for 2/5 of the time. How much of the night was she not dreaming?"""
    total_time_asleep = 10
    dream_time = (2/5) * total_time_asleep
    not_dream_time = total_time_asleep - dream_time
    result = not_dream_time
    return result

print(solution())