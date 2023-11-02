def solution():
    """Lily types 15 words a minute and takes a 2-minute break every 10 minutes. How long does it take for Lily to type 255 words?"""
    words_per_minute = 15
    words_to_type = 255
    time_to_type = words_to_type / words_per_minute
    num_breaks = time_to_type // 10
    total_break_time = num_breaks * 2
    total_time = time_to_type + total_break_time
    result = total_time
    return result

print(solution())