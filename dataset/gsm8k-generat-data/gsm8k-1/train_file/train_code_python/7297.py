def solution():
    """The tank of John's car is full: it contains 47 liters of gasoline. After a journey of 275 km, there are 14 liters left. What is the fuel consumption of this car per 100 km?"""
    starting_fuel = 47
    ending_fuel = 14
    distance = 275
    fuel_used = starting_fuel - ending_fuel
    fuel_per_100km = (fuel_used / distance) * 100
    result = fuel_per_100km
    return result

print(solution())