def solution():
    initial_fuel = 47
    final_fuel = 14
    distance_traveled = 275
    fuel_consumption = ((initial_fuel - final_fuel) / distance_traveled) * 100
    result = fuel_consumption
    return result

print(solution())