def solution():
    total_time = 1/6
    time_for_novels = total_time / 3
    time_for_graphic_novels = total_time / 3
    time_for_comic_books = total_time / 3
    
    pages_per_hour_novels = 21
    pages_per_hour_graphic_novels = 30
    pages_per_hour_comic_books = 45
    
    pages_read_novels = time_for_novels * pages_per_hour_novels
    pages_read_graphic_novels = time_for_graphic_novels * pages_per_hour_graphic_novels
    pages_read_comic_books = time_for_comic_books * pages_per_hour_comic_books
    
    result = pages_read_novels + pages_read_graphic_novels + pages_read_comic_books
    
    return result

print(solution())