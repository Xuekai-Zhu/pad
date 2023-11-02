def solution():
    """Emma is planning a dinner party, so she went to a shop to buy the products she needs. She bought 8 kg of cheese and 7 kg of vegetables. One kilogram of cheese costs $4 and one kilogram of vegetable costs is $2 more expensive. How much did she pay for her shopping?"""
    cheese_cost_per_kg = 4
    vegetable_cost_per_kg = cheese_cost_per_kg + 2
    cheese_weight = 8
    vegetable_weight = 7
    total_cost = (cheese_cost_per_kg * cheese_weight) + (vegetable_cost_per_kg * vegetable_weight)
    result = total_cost
    return result

print(solution())