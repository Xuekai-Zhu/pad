def solution():
    """Frank went to a shop to buy some food for his breakfast. He bought 10 buns for $0.1 each, two bottles of milk, for $2 each, and a carton of eggs, which was three times more expensive than one bottle of milk. How much did Frank pay for his breakfast shopping?"""
    buns = 10
    price_per_bun = 0.1
    milk_bottles = 2
    price_per_milk_bottle = 2
    price_per_egg_carton = price_per_milk_bottle * 3
    total_cost = (buns * price_per_bun) + (milk_bottles * price_per_milk_bottle) + price_per_egg_carton
    result = total_cost
    return result

print(solution())