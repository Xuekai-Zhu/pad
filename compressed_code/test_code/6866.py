def solution():
    
    micah_words_per_minute = 20
    isaiah_words_per_minute = 40
    micah_words_per_hour = micah_words_per_minute * 60
    isaiah_words_per_hour = isaiah_words_per_minute * 60
    difference = isaiah_words_per_hour - micah_words_per_hour
    result = difference
    return result

print(solution())