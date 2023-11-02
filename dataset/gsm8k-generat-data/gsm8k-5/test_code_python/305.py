def solution():
    books_needed = 8  # Tommy needs 8 new books
    cost_per_book = 5  # Each book costs $5
    current_savings = 13  # Tommy already has $13

    # Calculate the total cost of the books Tommy wants to buy
    total_cost = books_needed * cost_per_book

    # Calculate how much Tommy needs to save up
    amount_needed = total_cost - current_savings
    result = amount_needed
    return result

print(solution())