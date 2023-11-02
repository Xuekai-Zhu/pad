def solution():
    """Peter carried $500 to the market. He bought 6 kilos of potatoes for $2 per kilo, 9 kilos of tomato for $3 per kilo, 5 kilos of cucumbers for $4 per kilo, and 3 kilos of bananas for $5 per kilo. How much is Peter’s remaining money?"""
    total_cost = (6*2) + (9*3) + (5*4) + (3*5)
    remaining_money = 500 - total_cost
    result = remaining_money
    return result

print(solution())