def solution():
    """Fabian is shopping at a nearby supermarket. He wants to buy 5 kilograms of apples, 3 packs of sugar, and 500 grams of walnuts. One kilogram of apples costs $2, and one kilogram of walnuts costs $6. One pack of sugar is $1 cheaper than one kilogram of apples. How much Fabian needs to pay for the items he wants to buy?"""
    apple_weight = 5
    sugar_packs = 3
    walnut_weight = 0.5
    apple_price = 2
    sugar_price = apple_price - 1
    walnut_price = 6
    
    apple_cost = apple_weight * apple_price
    sugar_cost = sugar_packs * sugar_price
    walnut_cost = walnut_weight * walnut_price
    
    total_cost = apple_cost + sugar_cost + walnut_cost
    
    result = total_cost
    return result

print(solution())