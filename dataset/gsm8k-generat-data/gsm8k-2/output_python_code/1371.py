def solution():
    """Micah can type 20 words per minute and Isaiah can type 40 words per minute. How many more words can Isaiah type than Micah in an hour?"""
    micah_speed = 20
    isaiah_speed = 40
    minutes_in_hour = 60
    micah_total_words = micah_speed * minutes_in_hour
    isaiah_total_words = isaiah_speed * minutes_in_hour
    diff_words = isaiah_total_words - micah_total_words
    result = diff_words
    return result

print(solution())