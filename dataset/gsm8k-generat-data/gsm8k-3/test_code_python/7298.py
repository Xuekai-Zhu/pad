def solution():
    """The tank of John's car is full: it contains 47 liters of gasoline. After a journey of 275 km, there are 14 liters left. What is the fuel consumption of this car per 100 km?"""
    # Define the initial and final amount of gasoline in the tank
    initial_gas = 47
    final_gas = 14

    # Define the distance traveled
    distance = 275

    # Calculate the amount of gasoline used
    gas_used = initial_gas - final_gas

    # Calculate the fuel consumption per km
    fuel_consumption = gas_used / distance

    # Calculate the fuel consumption per 100 km
    fuel_consumption_100 = fuel_consumption * 100

    # Display the fuel consumption per 100 km
    result = fuel_consumption_100
    return result

print(solution())