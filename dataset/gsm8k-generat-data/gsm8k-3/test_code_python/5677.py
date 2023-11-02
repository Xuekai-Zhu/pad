def solution():
    """Tom can type 90 words a minute.  A page is 450 words.  How long would it take him to type out 10 pages?"""
    # Define the typing speed and number of words per page
    TYPING_SPEED = 90
    WORDS_PER_PAGE = 450

    # Define the number of pages to be typed
    number_of_pages = 10

    # Calculate the total number of words to be typed
    total_words = number_of_pages * WORDS_PER_PAGE

    # Calculate the time it will take to type all the words
    time_in_minutes = total_words / TYPING_SPEED

    # Display the time it will take
    result = time_in_minutes
    return result

print(solution())