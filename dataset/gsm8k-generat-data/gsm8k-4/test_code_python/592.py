def solution():
    """John uses 5 liters of fuel per km to travel. How many liters of fuel should John plan to use if he plans to travel on two trips of 30 km and 20 km?"""
    # Define the fuel usage per km and the distances of the trips
    fuel_per_km = 5
    trip1_distance = 30
    trip2_distance = 20

    # Calculate the total fuel needed for the trips
    total_fuel = fuel_per_km * (trip1_distance + trip2_distance)

    # Return the result
    result = total_fuel
    return result

print(solution())