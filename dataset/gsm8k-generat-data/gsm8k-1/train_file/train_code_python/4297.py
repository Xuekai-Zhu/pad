def solution():
    """Peter carried $500 to the market. He bought 6 kilos of potatoes for $2 per kilo, 9 kilos of tomato for $3 per kilo, 5 kilos of cucumbers for $4 per kilo, and 3 kilos of bananas for $5 per kilo. How much is Peter’s remaining money?"""
    initial_money = 500
    potato_cost = 2
    tomato_cost = 3
    cucumber_cost = 4
    banana_cost = 5
    total_cost = (6 * potato_cost) + (9 * tomato_cost) + (5 * cucumber_cost) + (3 * banana_cost)
    remaining_money = initial_money - total_cost
    result = remaining_money
    return result

print(solution())