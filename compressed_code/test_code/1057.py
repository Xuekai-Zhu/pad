def solution():
    
    micah_speed = 20
    isaiah_speed = 40
    minutes_in_hour = 60
    micah_total_words = micah_speed * minutes_in_hour
    isaiah_total_words = isaiah_speed * minutes_in_hour
    diff_words = isaiah_total_words - micah_total_words
    result = diff_words
    return result

print(solution())