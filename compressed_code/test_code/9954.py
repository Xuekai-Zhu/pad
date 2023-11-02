def solution():
    
    words_per_minute = 40
    words_per_page = 100
    pages_per_book = 80
    reading_time = 20 * 60  
    words_per_book = words_per_page * pages_per_book
    total_words = reading_time * words_per_minute
    books_needed = total_words / words_per_book
    result = round(books_needed)
    
    return result

print(solution())