def solution():
    """Jack went to a supermarket with $100 and bought 4 bottles of water. 
    Then his mother called him and asked him to buy twice as many bottles as he already bought. 
    Each bottle cost $2. Finally, he also bought half a pound of cheese and 1 pound of cheese costs $10. 
    How much money does Jack have remaining?"""
    starting_money = 100
    water_bottles = 4
    additional_bottles = 2 * water_bottles
    bottle_cost = 2
    cheese_cost_per_pound = 10
    cheese_weight = 0.5
    total_spent = (water_bottles + additional_bottles) * bottle_cost + cheese_weight * cheese_cost_per_pound
    remaining_money = starting_money - total_spent
    result = remaining_money
    return result

print(solution())