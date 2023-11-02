def solution():
    """Sarah is checking out books from the library to read on vacation. She can read 40 words per minute. The books she is checking out have 100 words per page and are 80 pages long. She will be reading for 20 hours. How many books should she check out?"""
    # Define the reading speed and book characteristics
    SPEED = 40 # words per minute
    WORDS_PER_PAGE = 100
    PAGES_PER_BOOK = 80

    # Calculate the total number of words Sarah can read in 20 hours
    total_time_minutes = 20 * 60
    total_words_can_read = total_time_minutes * SPEED

    # Calculate the total number of pages Sarah can read in 20 hours
    total_pages_can_read = total_words_can_read / WORDS_PER_PAGE

    # Calculate the number of books Sarah should check out
    books_to_checkout = total_pages_can_read / PAGES_PER_BOOK

    # Round up to the nearest whole number
    books_to_checkout = int(books_to_checkout) + 1

    # Display the number of books Sarah should check out
    result = books_to_checkout
    return result

print(solution())