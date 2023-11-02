def solution():
    """Barbara Blackburn can type 212 words per minute. Due to Carpal tunnel syndrome, Barbara cannot use her left hand for a while so her typing speed is now 40 words less per minute. If she is supposed to type a document with 3440 words, how many minutes will it take her to finish typing the document?"""
    words_per_minute = 212 - 40
    total_words = 3440
    minutes_to_type = total_words / words_per_minute
    result = minutes_to_type
    return result

print(solution())