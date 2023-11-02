def solution():
    """You can buy 4 apples or 1 watermelon for the same price. You bought 36 fruits evenly split between oranges, apples and watermelons, and the price of 1 orange is $0.50. How much does 1 apple cost if your total bill was $66?"""
    orange_price = 0.5
    total_fruits = 36
    apples = total_fruits / 6
    watermelons = total_fruits / 6
    oranges = total_fruits / 2
    price_per_fruit = 66 / total_fruits
    apple_price = (4 * price_per_fruit - price_per_fruit) / 3
    result = apple_price
    return result

print(solution())