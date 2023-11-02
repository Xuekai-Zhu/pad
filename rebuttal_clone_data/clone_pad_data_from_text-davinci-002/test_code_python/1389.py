def solution():
    words_before = 10
    words_after = 8
    minutes = 5
    words_before_5_minutes = words_before * minutes
    words_after_5_minutes = words_after * minutes
    difference = words_before_5_minutes - words_after_5_minutes
    result = difference
    return result

print(solution())