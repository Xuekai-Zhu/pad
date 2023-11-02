def solution():
    """Sarah is checking out books from the library to read on vacation. She can read 40 words per minute. The books she is checking out have 100 words per page and are 80 pages long. She will be reading for 20 hours. How many books should she check out?"""
    # Define the reading speed in words per minute, the number of words per page, and the number of pages in each book
    words_per_minute = 40
    words_per_page = 100
    pages_per_book = 80

    # Calculate the number of words Sarah can read in 20 hours
    words_per_hour = words_per_minute * 60
    total_words = words_per_hour * 20

    # Calculate the number of books Sarah can read
    total_pages = total_words / words_per_page
    total_books = total_pages / pages_per_book

    # Round up to the nearest integer and return the result
    result = int(total_books + 0.5)
    return result

print(solution())