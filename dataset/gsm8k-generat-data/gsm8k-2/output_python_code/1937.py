def solution():
    """Alicia has to buy some books for the new school year. She buys 2 math books, 3 art books, and 6 science books, for a total of $30. If both the math and science books cost $3 each, what was the cost of each art book?"""
    total_books = 2 + 3 + 6
    total_cost = 30
    math_and_science_cost = 2 * 3 + 6 * 3
    art_book_cost = (total_cost - math_and_science_cost) / 3
    result = art_book_cost
    return result

print(solution())