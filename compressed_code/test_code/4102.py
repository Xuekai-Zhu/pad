def solution():
    
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