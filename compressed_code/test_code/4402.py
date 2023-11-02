def solution():
    
    tank_size = 150
    starting_fuel = 38
    fuel_needed = tank_size - starting_fuel
    fuel_cost = 3
    total_cost = fuel_needed * fuel_cost
    change = 350 - total_cost
    result = change
    return result

print(solution())