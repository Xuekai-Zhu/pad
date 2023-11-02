def solution():
    words_per_minute = 90
    words_per_page = 450
    pages_to_type = 10
    typing_time = pages_to_type * words_per_page / words_per_minute
    result = typing_time
    return result

print(solution())