def solution():
    """The tank of John's car is full: it contains 47 liters of gasoline. After a journey of 275 km, there are 14 liters left. What is the fuel consumption of this car per 100 km?"""
    initial_fuel = 47
    remaining_fuel = 14
    distance = 275
    fuel_used = initial_fuel - remaining_fuel
    fuel_per_km = fuel_used / distance
    fuel_per_100km = fuel_per_km * 100
    result = fuel_per_100km
    return result

print(solution())