def solution():
    """Jaydee can type 38 words in a minute. How many hours will he take to finish typing a research paper with 4560 words?"""
    words_per_minute = 38
    total_words = 4560
    minutes_to_type = total_words / words_per_minute
    hours_to_type = minutes_to_type / 60
    result = hours_to_type
    return result

print(solution())