def solution():
    """Emma is planning a dinner party, so she went to a shop to buy the products she needs. She bought 8 kg of cheese and 7 kg of vegetables. One kilogram of cheese costs $4 and one kilogram of vegetable costs is $2 more expensive. How much did she pay for her shopping?"""
    cheese_price = 4
    vegetable_price = cheese_price + 2
    cheese_weight = 8
    vegetable_weight = 7
    total_cheese_price = cheese_price * cheese_weight
    total_vegetable_price = vegetable_price * vegetable_weight
    total_price = total_cheese_price + total_vegetable_price
    result = total_price
    return result

print(solution())