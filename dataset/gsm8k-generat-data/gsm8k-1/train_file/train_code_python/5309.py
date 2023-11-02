def solution():
    """Sarah is checking out books from the library to read on vacation. She can read 40 words per minute. The books she is checking out have 100 words per page and are 80 pages long. She will be reading for 20 hours. How many books should she check out?"""
    words_per_minute = 40
    words_per_page = 100
    pages_per_book = 80
    reading_time = 20 * 60  # convert 20 hours to minutes
    words_per_book = words_per_page * pages_per_book
    total_words = reading_time * words_per_minute
    books_needed = total_words / words_per_book
    result = round(books_needed)
    
    return result

print(solution())