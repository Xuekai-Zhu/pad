def solution():
    """Gunther can type 160 words every 3 minutes and he works 480 minutes per day. How many words can Gunther type in a working day?"""
    words_per_minute = 160 / 3
    minutes_per_day = 480
    total_words = words_per_minute * minutes_per_day
    result = total_words
    return result

print(solution())