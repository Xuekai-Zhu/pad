def solution():
    """Anna is trying to buy books for her local library. She had a budget of $16, and she has already spent $4. She also bought 2 books today, and both books cost her the same amount of money. If Anna has $2 left in her budget, how much did each of the books cost?"""
    total_budget = 16
    amount_spent = 4
    remaining_budget = 2
    num_books = 2
    cost_per_book = (total_budget - amount_spent - remaining_budget) / num_books
    result = cost_per_book
    return result

print(solution())