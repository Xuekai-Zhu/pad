def solution():
    words_per_minute = 90  # Tom types 90 words per minute
    words_per_page = 450  # A page has 450 words
    pages = 10  # Tom wants to know how long it will take him to type out 10 pages

    # Calculate the total number of words to be typed
    total_words = words_per_page * pages

    # Calculate the total time required to type the given number of words
    total_time = total_words / words_per_minute

    result = total_time
    return result

print(solution())