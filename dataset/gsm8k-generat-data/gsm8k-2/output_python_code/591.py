def solution():
    """John uses 5 liters of fuel per km to travel. How many liters of fuel should John plan to use if he plans to travel on two trips of 30 km and 20 km?"""
    fuel_rate = 5
    trip1_distance = 30
    trip2_distance = 20
    total_distance = trip1_distance + trip2_distance
    total_fuel = fuel_rate * total_distance
    result = total_fuel
    return result

print(solution())