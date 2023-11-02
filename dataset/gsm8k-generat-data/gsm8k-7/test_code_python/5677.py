def solution():
    words_per_minute = 90
    words_per_page = 450
    num_pages = 10

    # Calculate the total number of words to be typed
    total_words = num_pages * words_per_page

    # Calculate the time it takes to type out all words in minutes
    time_in_minutes = total_words / words_per_minute

    result = time_in_minutes
    return result

print(solution())