def solution():
    """Theo bought a pen for $2 and a piece of paper that cost $1 less than three times the price of the pen. She gave the cashier $10. What is the amount of change Theo received?"""
    pen_price = 2
    paper_price = 3 * pen_price - 1
    total_cost = pen_price + paper_price
    amount_paid = 10
    change = amount_paid - total_cost
    result = change
    return result

print(solution())