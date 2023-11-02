def solution():
    free_time_hours = 8
    game_play_hours = free_time_hours * (75 / 100)
    reading_hours = free_time_hours - game_play_hours
    pages_read_per_hour = 60
    book_page_length = 80
    books_read = reading_hours * pages_read_per_hour / book_page_length
    result = books_read
    return result

print(solution())