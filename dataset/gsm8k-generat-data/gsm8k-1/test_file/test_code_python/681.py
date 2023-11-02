def solution():
    """Catherine goes to the grocery store. She buys 1 kilo of apples for $4, 2 kilos of bananas for $2 per kilo, and 2 kilos of oranges for $3 per kilo. How many dollars does she pay in total?"""
    apple_price = 4
    banana_price = 2
    orange_price = 3
    apple_weight = 1
    banana_weight = 2
    orange_weight = 2
    total_cost = (apple_price * apple_weight) + (banana_price * banana_weight) + (orange_price * orange_weight)
    result = total_cost
    return result

print(solution())