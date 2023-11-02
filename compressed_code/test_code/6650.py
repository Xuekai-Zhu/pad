def solution():
    
    tiles_on_monday = 38
    books_on_monday = 75
    tiles_on_tuesday = tiles_on_monday * 2
    books_on_tuesday = books_on_monday * 3
    total_count_on_tuesday = tiles_on_tuesday + books_on_tuesday
    result = total_count_on_tuesday
    return result

print(solution())