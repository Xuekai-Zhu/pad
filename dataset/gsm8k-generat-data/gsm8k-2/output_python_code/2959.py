def solution():
    """Emily can type 60 words per minute. How many hours does it take her to write 10,800 words?"""
    words_typed = 10800
    typing_speed = 60  # words per minute
    total_time = words_typed / typing_speed / 60  # time in hours
    result = total_time
    return result

print(solution())