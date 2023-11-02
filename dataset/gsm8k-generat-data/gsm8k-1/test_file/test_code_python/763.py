def solution():
    """To make 1 liter of juice, Sam needs 5 kilograms of oranges. Each kilogram of oranges costs $3. How much money would Sam have to spend to make 4 liters of juice?"""
    oranges_per_liter = 5
    cost_per_orange = 3
    liters_of_juice = 4
    total_cost = oranges_per_liter * cost_per_orange * liters_of_juice
    result = total_cost
    return result

print(solution())