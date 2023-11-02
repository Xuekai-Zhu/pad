def solution():
    """Mary went to the store to buy fruit. Apples cost $1, oranges cost $2, and bananas cost $3. For every 5 fruits that customers buy, the store offers a $1 discount. Mary buys 5 apples, 3 oranges, and 2 bananas. How much will she pay?"""
    apple_cost = 1
    orange_cost = 2
    banana_cost = 3
    total_fruits = 5 + 3 + 2
    total_cost = (5 * apple_cost) + (3 * orange_cost) + (2 * banana_cost)
    if total_fruits >= 5:
        discount = (total_fruits // 5) * 1
        total_cost -= discount
    result = total_cost
    return result

print(solution())