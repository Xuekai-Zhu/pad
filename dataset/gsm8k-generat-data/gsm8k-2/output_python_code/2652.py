def solution():
    """Mary and her two friends agreed to evenly pay for the cost of 2 pounds of chicken. Mary's mother went to the grocery and bought the 2-pound chicken, 3 pounds of beef that cost $4 per pound, and a liter of oil that costs $1. If Mary's mother paid a total of $16 for the grocery, how much should Mary and her two friends pay each for the chicken?"""
    chicken_weight = 2
    beef_weight = 3
    beef_price_per_pound = 4
    oil_price = 1
    total_price = 16

    chicken_price_per_pound = (total_price - (beef_weight * beef_price_per_pound) - oil_price) / chicken_weight
    price_per_person = round(chicken_price_per_pound / 3, 2)

    result = price_per_person
    return result

print(solution())