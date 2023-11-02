def solution():
    """James decides to pick some blueberries. It cost $20 to go picking and then another $1.5 per pound. He picked 30 pounds of blueberries. How much did he save compared to buying at the store for $2.5 a pound?"""
    picking_cost = 20
    per_pound_cost = 1.5
    pounds_picked = 30
    total_cost = picking_cost + (per_pound_cost * pounds_picked)
    store_cost = 2.5 * pounds_picked
    savings = store_cost - total_cost
    result = savings
    return result

print(solution())