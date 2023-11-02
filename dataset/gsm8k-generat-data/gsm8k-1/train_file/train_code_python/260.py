def solution():
    """You can buy 4 apples or 1 watermelon for the same price. You bought 36 fruits evenly split between oranges, apples and watermelons, and the price of 1 orange is $0.50. How much does 1 apple cost if your total bill was $66?"""
    total_fruits = 36
    oranges = total_fruits // 3
    apples = total_fruits // 3
    watermelons = total_fruits // 3
    orange_price = 0.5
    total_orange_cost = oranges * orange_price
    total_cost = 66
    apple_cost = (total_cost - total_orange_cost) / apples
    result = apple_cost
    return result

print(solution())