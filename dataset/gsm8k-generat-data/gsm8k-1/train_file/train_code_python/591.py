def solution():
    """John uses 5 liters of fuel per km to travel. How many liters of fuel should John plan to use if he plans to travel on two trips of 30 km and 20 km?"""
    fuel_per_km = 5
    distance_1 = 30
    distance_2 = 20
    total_distance = distance_1 + distance_2
    total_fuel = fuel_per_km * total_distance
    result = total_fuel
    return result

print(solution())