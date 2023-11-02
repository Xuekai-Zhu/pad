def solution():
    
    total_books = 2 + 3 + 6
    total_cost = 30
    math_and_science_cost = 2 * 3 + 6 * 3
    art_book_cost = (total_cost - math_and_science_cost) / 3
    result = art_book_cost
    return result

print(solution())