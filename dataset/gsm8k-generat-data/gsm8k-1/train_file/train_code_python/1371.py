def solution():
    """Micah can type 20 words per minute and Isaiah can type 40 words per minute. How many more words can Isaiah type than Micah in an hour?"""
    micah_words_per_minute = 20
    isaiah_words_per_minute = 40
    micah_words_per_hour = micah_words_per_minute * 60
    isaiah_words_per_hour = isaiah_words_per_minute * 60
    difference = isaiah_words_per_hour - micah_words_per_hour
    result = difference
    return result

print(solution())