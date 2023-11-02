def solution():
    """The price of two kilograms of sugar and five kilograms of salt is $5.50.
    If a kilogram of sugar costs $1.50, then how much is the price of three kilograms of sugar and a kilogram of salt?"""
    sugar_price_per_kg = 1.5
    salt_price_per_kg = (5.5 - 2 * sugar_price_per_kg) / 5
    total_price = 3 * sugar_price_per_kg + salt_price_per_kg
    result = total_price
    return result

print(solution())