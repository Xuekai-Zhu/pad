def solution():
    """Tom can type 90 words a minute. A page is 450 words. How long would it take him to type out 10 pages?"""
    # Define the number of words Tom can type per minute
    words_per_minute = 90

    # Define the number of words per page
    words_per_page = 450

    # Define the number of pages to be typed
    pages_to_type = 10

    # Calculate the total number of words to be typed
    total_words = words_per_page * pages_to_type

    # Calculate the number of minutes it would take to type all the words
    minutes_to_type = total_words / words_per_minute

    # Return the result
    result = minutes_to_type
    return result

print(solution())