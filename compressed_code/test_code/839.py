def solution():
    
    monday_tiles_count = 38
    monday_books_count = 75
    tuesday_tiles_count = 2 * monday_tiles_count
    tuesday_books_count = 3 * monday_books_count
    total_count = tuesday_tiles_count + tuesday_books_count
    result = total_count
    return result

print(solution())