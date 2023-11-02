def solution():
    """Marcia wants to buy some fruit. Apples cost $2, bananas cost $1, and oranges cost $3. If Marcia buys 12 apples, 4 bananas and 4 oranges, what is the average cost of each piece of fruit in dollars?"""
    apple_cost = 2
    banana_cost = 1
    orange_cost = 3
    total_cost = (12 * apple_cost) + (4 * banana_cost) + (4 * orange_cost)
    total_pieces = 12 + 4 + 4
    average_cost = total_cost / total_pieces
    result = average_cost
    return result

print(solution())