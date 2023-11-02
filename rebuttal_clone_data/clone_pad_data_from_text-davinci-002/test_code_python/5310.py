def solution():
    words_per_minute = 40
    words_per_page = 100
    pages_per_book = 80
    minutes_per_hour = 60
    hours_reading = 20
    minutes_reading = hours_reading * minutes_per_hour
    total_words_read = words_per_minute * minutes_reading
    total_pages_read = total_words_read / words_per_page
    total_books = total_pages_read / pages_per_book
    result = total_books
    
    return result

print(solution())