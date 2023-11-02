def solution():
    """Jack went to a supermarket with $100 and bought 4 bottles of water. Then his mother called him and asked him to buy twice as many bottles as he already bought. Each bottle cost $2. Finally, he also bought half a pound of cheese and 1 pound of cheese costs $10. How much money does Jack have remaining?"""
    initial_money = 100
    water_cost = 4
    water_qty = 8
    water_total_cost = water_qty * water_cost
    cheese_qty = 0.5
    cheese_cost = 10
    cheese_total_cost = cheese_qty * cheese_cost
    total_cost = water_total_cost + cheese_total_cost
    remaining_money = initial_money - total_cost
    result = remaining_money
    return result

print(solution())