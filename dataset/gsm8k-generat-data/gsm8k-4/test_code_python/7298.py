def solution():
    """The tank of John's car is full: it contains 47 liters of gasoline. After a journey of 275 km, there are 14 liters left. What is the fuel consumption of this car per 100 km?"""
    # Define the initial amount of gasoline and the amount left after the journey
    initial_gasoline = 47
    remaining_gasoline = 14

    # Calculate the total gasoline consumed during the journey
    consumed_gasoline = initial_gasoline - remaining_gasoline

    # Calculate the fuel consumption per kilometer
    fuel_consumption_per_km = consumed_gasoline / 275

    # Calculate the fuel consumption per 100 km
    fuel_consumption_per_100km = fuel_consumption_per_km * 100

    # Return the result
    result = fuel_consumption_per_100km
    return result

print(solution())