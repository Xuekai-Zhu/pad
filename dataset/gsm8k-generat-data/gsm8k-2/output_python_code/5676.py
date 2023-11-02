def solution():
    """Tom can type 90 words a minute. A page is 450 words. How long would it take him to type out 10 pages?"""
    words_per_minute = 90
    words_per_page = 450
    pages_to_type = 10
    total_words = words_per_page * pages_to_type
    time_in_minutes = total_words / words_per_minute
    result = time_in_minutes
    return result

print(solution())