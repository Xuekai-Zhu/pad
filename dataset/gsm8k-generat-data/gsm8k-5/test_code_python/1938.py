def solution():
    math_books = 2
    science_books = 6
    art_books = 3
    total_books = math_books + science_books + art_books

    cost_of_math_and_science = (math_books + science_books) * 3
    total_cost = 30
    cost_of_art_books = (total_cost - cost_of_math_and_science) / art_books

    result = cost_of_art_books
    return result

print(solution())