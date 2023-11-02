def solution():
    liters_of_diesel = 36
    value_of_diesel = 18
    tank_size = 64
    full_tank_cost = tank_size * (value_of_diesel / liters_of_diesel)
    result = full_tank_cost
    return result

print(solution())