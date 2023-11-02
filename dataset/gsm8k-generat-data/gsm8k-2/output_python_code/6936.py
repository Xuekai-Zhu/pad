def solution():
    """The price of two kilograms of sugar and five kilograms of salt is $5.50. If a kilogram of sugar costs $1.50, then how much is the price of three kilograms of sugar and a kilogram of salt?"""
    sugar_price = 1.5
    salt_price = (5.5 - 2*sugar_price) / 5
    total_price = 3*sugar_price + salt_price
    result = total_price
    return result

print(solution())