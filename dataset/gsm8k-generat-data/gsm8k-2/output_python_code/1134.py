def solution():
    """Reggie's father gave him $48. Reggie bought 5 books, each of which cost $2. How much money does Reggie have left?"""
    initial_money = 48
    book_cost = 2
    total_book_cost = book_cost * 5
    remaining_money = initial_money - total_book_cost
    result = remaining_money
    return result

print(solution())