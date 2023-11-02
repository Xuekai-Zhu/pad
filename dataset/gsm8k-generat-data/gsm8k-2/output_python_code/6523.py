def solution():
    """Lynne bought 7 books about cats and 2 books about the solar system. She also bought 3 magazines. Each book cost 7$ and each magazine cost $4. How much did Lynne spend in all?"""
    book_cost = 7
    magazine_cost = 4
    total_book_cost = (7 * book_cost) + (2 * book_cost)
    total_magazine_cost = 3 * magazine_cost
    total_cost = total_book_cost + total_magazine_cost
    result = total_cost
    return result

print(solution())