def solution():
    """Sarah is checking out books from the library to read on vacation. She can read 40 words per minute. The books she is checking out have 100 words per page and are 80 pages long. She will be reading for 20 hours. How many books should she check out?"""
    words_per_minute = 40
    words_per_page = 100
    pages_per_book = 80
    hours_available = 20
    words_per_hour = words_per_minute * 60
    words_per_book = words_per_page * pages_per_book
    books_per_hour = words_per_hour / words_per_book
    total_books = books_per_hour * hours_available
    result = round(total_books)
    return result

print(solution())