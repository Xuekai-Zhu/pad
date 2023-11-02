def solution():
    words_per_minute = 15
    words_to_type = 255
    minutes_per_break = 2
    minutes_between_breaks = 10
    minutes_typing = (words_to_type / words_per_minute) + ((words_to_type / words_per_minute) / minutes_between_breaks) * minutes_per_break
    result = minutes_typing
    return result

print(solution())