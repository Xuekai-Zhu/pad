def solution():
    total_fuel = 150
    current_fuel = 38
    cost_per_liter = 3
    total_cost = (total_fuel - current_fuel) * cost_per_liter
    change = 350 - total_cost
    result = change
    return result

print(solution())