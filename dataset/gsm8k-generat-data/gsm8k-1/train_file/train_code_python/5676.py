def solution():
    """Tom can type 90 words a minute. A page is 450 words. How long would it take him to type out 10 pages?"""
    words_per_minute = 90
    words_per_page = 450
    pages_to_type = 10
    total_words_to_type = words_per_page * pages_to_type
    minutes_to_type = total_words_to_type / words_per_minute
    result = minutes_to_type
    
    return result

print(solution())