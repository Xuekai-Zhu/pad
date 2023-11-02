def solution():
    """John uses 5 liters of fuel per km to travel. How many liters of fuel should John plan to use if he plans to travel on two trips of 30 km and 20 km?"""
    # Define the fuel consumption rate
    FUEL_CONSUMPTION = 5 # liters per km

    # Define the distances to be traveled
    distance1 = 30 # km
    distance2 = 20 # km

    # Calculate the fuel usage for each trip
    fuel_usage1 = FUEL_CONSUMPTION * distance1
    fuel_usage2 = FUEL_CONSUMPTION * distance2

    # Calculate the total fuel usage for both trips
    total_fuel_usage = fuel_usage1 + fuel_usage2

    # Display the total fuel usage
    result = total_fuel_usage
    return result

print(solution())