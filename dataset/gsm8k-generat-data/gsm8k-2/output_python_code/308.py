def solution():
    """Carl types at a speed of 50 words per minute. If he types continuously for 4 hours per day, how many words can he type in 7 days?"""
    words_per_minute = 50
    minutes_per_hour = 60
    hours_per_day = 4
    days = 7
    total_minutes = minutes_per_hour * hours_per_day * days
    total_words = words_per_minute * total_minutes
    result = total_words
    return result

print(solution())