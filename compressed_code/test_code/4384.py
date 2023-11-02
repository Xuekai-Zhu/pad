def solution():
    
    words_per_minute = 90
    words_per_page = 450
    pages_to_type = 10
    total_words = words_per_page * pages_to_type
    time_in_minutes = total_words / words_per_minute
    result = time_in_minutes
    return result

print(solution())