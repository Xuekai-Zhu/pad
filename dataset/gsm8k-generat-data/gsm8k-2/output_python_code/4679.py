def solution():
    """Adam bought 3 kilograms of nuts and 2.5 kilograms of dried fruits at a store. One kilogram of nuts costs $12 and one kilogram of dried fruit costs $8. How much did his purchases cost?"""
    nuts_price = 12
    dried_fruit_price = 8
    nuts_weight = 3
    dried_fruit_weight = 2.5
    total_nuts_price = nuts_price * nuts_weight
    total_dried_fruit_price = dried_fruit_price * dried_fruit_weight
    total_price = total_nuts_price + total_dried_fruit_price
    result = total_price
    return result

print(solution())