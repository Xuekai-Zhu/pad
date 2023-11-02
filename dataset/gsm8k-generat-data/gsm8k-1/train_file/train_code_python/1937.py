def solution():
    """Alicia has to buy some books for the new school year. She buys 2 math books, 3 art books, and 6 science books, for a total of $30. If both the math and science books cost $3 each, what was the cost of each art book?"""
    math_books = 2
    science_books = 6
    art_books = 3
    total_cost = 30
    cost_math_and_science = (math_books + science_books) * 3
    cost_art_books = (total_cost - cost_math_and_science) / art_books
    result = cost_art_books
    return result

print(solution())