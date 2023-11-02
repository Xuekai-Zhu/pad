def solution():
    
    top_level_books = 64
    level_three_books = top_level_books / 0.8
    level_two_books = level_three_books / 0.8
    level_one_books = level_two_books / 0.8
    total_books = top_level_books + level_three_books + level_two_books + level_one_books
    result = total_books
    return result

print(solution())