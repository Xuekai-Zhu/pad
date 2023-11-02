def solution():
    """Mary went to the store to buy fruit. Apples cost $1, oranges cost $2, and bananas cost $3. For every 5 fruits that customers buy, the store offers a $1 discount. Mary buys 5 apples, 3 oranges, and 2 bananas. How much will she pay?"""
    apple_price = 1
    orange_price = 2
    banana_price = 3
    total_fruits = 5 + 3 + 2
    total_price = (apple_price * 5) + (orange_price * 3) + (banana_price * 2)
    discount = (total_fruits // 5) * 1
    final_price = total_price - discount
    result = final_price
    return result

print(solution())