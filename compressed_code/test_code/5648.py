def solution():
    
    initial_fuel = 47
    remaining_fuel = 14
    distance = 275
    fuel_used = initial_fuel - remaining_fuel
    fuel_per_km = fuel_used / distance
    fuel_per_100km = fuel_per_km * 100
    result = fuel_per_100km
    return result

print(solution())