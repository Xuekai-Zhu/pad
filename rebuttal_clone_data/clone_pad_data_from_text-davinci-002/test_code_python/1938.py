def solution():
    num_math_books = 2
    num_art_books = 3
    num_science_books = 6
    cost_of_books = 30
    cost_of_math_books = num_math_books * 3
    cost_of_science_books = num_science_books * 3
    cost_of_art_books = cost_of_books - cost_of_math_books - cost_of_science_books
    result = cost_of_art_books
    return result

print(solution())